# A3 — Polyglot Fraud Score Pipeline

| Component | Stack | Role |
|-----------|-------|------|
| `api/` | FastAPI | Ingest events, accept scores |
| `worker/` | Node.js | Poll pending, invoke scorer, PATCH results |
| `scorer/` | Rust CLI | JSON in → risk score out |

## Verify

```bash
cd api && pip install -r requirements.txt && pytest -v
cd ../scorer && cargo test
cd ../worker && npm run poll   # requires API running on :8001
```

## Three-terminal demo

```bash
# T1
cd api && uvicorn main:app --port 8001

# T2
cd scorer && cargo build

# T3
curl -X POST localhost:8001/events -H 'Content-Type: application/json' \
  -d '{"account_id":"u1","value":8000,"channel":"wire"}'
cd worker && FRAUD_API=http://127.0.0.1:8001 SCORER_BIN=../scorer/target/debug/fraud-scorer node worker.js
```
