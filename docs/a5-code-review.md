# A5 — Code Review

**Subject:** B4 balance API (`exercises/b4-balance-api/main.py`)  
**Reviewer:** Atul (assessment exercise)

## Summary

Clean minimal FastAPI service. Suitable for B4 baseline. Several improvements recommended before production.

## Findings

| ID | Severity | Finding | Recommendation |
|----|----------|---------|----------------|
| R1 | Medium | In-memory store — data lost on restart | Document limitation; use DB for persistence |
| R2 | Medium | No idempotency or auth on POST | Add API key or scope for write endpoints |
| R3 | Low | Global mutable state | Acceptable for demo; inject store for testability |
| R4 | Low | `round(balance, 2)` only on GET | Consider decimal type for money |
| R5 | Info | Missing OpenAPI examples | Add `Field(examples=...)` for reviewer UX |
| R6 | Info | No health endpoint | Add `/health` for k8s probes (see D4) |

## Positive observations

- Pydantic validation on amount (`gt=0`)
- Insufficient funds guard on debit
- Explicit `reset()` for test isolation
- Newest-first transaction ordering is intuitive

## Suggested patch (health check)

```python
@app.get("/health")
def health():
    return {"status": "ok", "transactions": len(_ledger)}
```

Non-blocking for assessment scope.

## Verdict

**Approve for assessment** with documented limitations. No security-sensitive data handled.

## Review method

Findings were captured by reading the B4 implementation directly; persistence and money-precision gaps are noted above.
