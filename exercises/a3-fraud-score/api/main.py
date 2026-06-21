from datetime import datetime, timezone

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Fraud Ingest API")

_events: dict[str, dict] = {}
_counter = 1


class EventIn(BaseModel):
    account_id: str
    value: float = Field(gt=0)
    channel: str
    ts: datetime | None = None


class EventOut(EventIn):
    event_id: str
    ts: datetime
    state: str


class ScorePatch(BaseModel):
    event_id: str
    score: float = Field(ge=0, le=1)
    band: str
    flags: list[str] = []


@app.get("/health")
def health():
    return {"service": "ingest", "pending": sum(1 for e in _events.values() if e["state"] == "pending")}


@app.post("/events", response_model=EventOut, status_code=201)
def create_event(body: EventIn):
    global _counter
    eid = f"ev-{_counter}"
    _counter += 1
    row = EventOut(
        event_id=eid,
        account_id=body.account_id,
        value=body.value,
        channel=body.channel,
        ts=body.ts or datetime.now(timezone.utc),
        state="pending",
    )
    _events[eid] = row.model_dump(mode="json")
    return row


@app.get("/events")
def list_events(state: str | None = None):
    rows = list(_events.values())
    if state:
        rows = [r for r in rows if r["state"] == state]
    return rows


@app.patch("/events/{event_id}/score", response_model=EventOut)
def attach_score(event_id: str, body: ScorePatch):
    row = _events.get(event_id)
    if not row:
        raise HTTPException(404, "event not found")
    if body.event_id != event_id:
        raise HTTPException(400, "event_id mismatch")
    row.update({"state": "scored", "score": body.score, "band": body.band, "flags": body.flags})
    return EventOut(**row)


def reset():
    global _events, _counter
    _events, _counter = {}, 1
