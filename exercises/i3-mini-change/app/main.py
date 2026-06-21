from fastapi import FastAPI, Query

app = FastAPI(title="I3 Mini Change")

_NOTES = [{"id": i, "text": f"note-{i}"} for i in range(1, 21)]


@app.get("/notes")
def list_notes(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=50),
):
    """Added pagination params (I3 safe change)."""
    return _NOTES[skip : skip + limit]


@app.get("/notes/{note_id}")
def get_note(note_id: int):
    for n in _NOTES:
        if n["id"] == note_id:
            return n
    return {"detail": "not found"}
