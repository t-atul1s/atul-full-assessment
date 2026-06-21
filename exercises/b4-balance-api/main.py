"""B4 — FastAPI balance API (in-memory ledger)."""
from datetime import datetime, timezone
from typing import Literal

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Balance API", version="1.0.0")

_ledger: list[dict] = []
_balance: float = 0.0
_seq: int = 1


class TxIn(BaseModel):
    kind: Literal["credit", "debit"]
    amount: float = Field(gt=0, description="Positive amount")
    note: str | None = None


class TxOut(TxIn):
    id: int
    at: datetime


@app.post("/transactions", response_model=TxOut, status_code=201)
def post_transaction(body: TxIn) -> TxOut:
    global _balance, _seq

    if body.kind == "debit" and body.amount > _balance:
        raise HTTPException(status_code=400, detail="Insufficient funds")

    row = TxOut(
        id=_seq,
        kind=body.kind,
        amount=body.amount,
        note=body.note,
        at=datetime.now(timezone.utc),
    )
    _seq += 1
    _ledger.append(row.model_dump())

    _balance += body.amount if body.kind == "credit" else -body.amount
    return row


@app.get("/transactions", response_model=list[TxOut])
def get_transactions() -> list[TxOut]:
    return [TxOut(**row) for row in reversed(_ledger)]


@app.get("/balance")
def get_balance() -> dict[str, float]:
    return {"balance": round(_balance, 2)}


def reset() -> None:
    global _ledger, _balance, _seq
    _ledger, _balance, _seq = [], 0.0, 1
