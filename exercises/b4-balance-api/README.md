# B4 — FastAPI Balance API

In-memory ledger with credit/debit transactions and running balance.

## Run

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## Verify

```bash
pytest tests/ -v
```

## curl

```bash
curl -X POST localhost:8000/transactions -H 'Content-Type: application/json' \
  -d '{"kind":"credit","amount":500}'
curl localhost:8000/balance
```
