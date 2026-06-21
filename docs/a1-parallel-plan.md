# A1 — Parallel Worktree Plan

**Base project:** B4 balance API (`exercises/b4-balance-api`)  
**Goal:** Two parallel feature lanes merged into an integration branch without breaking tests.

## Task decomposition

| Lane | Branch | Feature | Files touched |
|------|--------|---------|---------------|
| A | `feature/tx-by-id` | GET `/transactions/{id}` | `main.py`, `tests/test_api.py` |
| B | `feature/balance-summary` | GET `/summary` with tx count + balance | `main.py`, `tests/test_api.py` |
| Integration | `exercise/a2-worktrees` | Merge A then B, resolve test conflicts | all above |

## Parallel lane specifications

**Lane A:**
> Add GET `/transactions/{id}` returning 404 when missing. Extend pytest with lookup + not-found cases. Do not modify list or balance endpoints.

**Lane B:**
> Add GET `/summary` returning `{balance, count}`. Add tests. Do not add by-id route.

## Shared constraints

- Keep in-memory store pattern
- Preserve existing endpoint contracts
- All tests must pass after merge
- No new dependencies

## Merge order

1. Branch `exercise/a2-worktrees` from B4 baseline
2. Merge `feature/tx-by-id` → run pytest
3. Merge `feature/balance-summary` → resolve `tests/test_api.py` conflict (keep both test classes)
4. Final pytest gate

## Conflict plan

Likely conflict: both lanes append tests to `tests/test_api.py`. Resolution: keep both test functions, shared `reset()` fixture unchanged.

## Verification plan

```bash
cd exercises/b4-balance-api
pytest tests/ -v   # expect 7+ tests after merge
curl localhost:8000/summary
curl localhost:8000/transactions/1
```

## Worktree commands (reference)

```bash
git worktree add ../wt-a feature/tx-by-id
git worktree add ../wt-b feature/balance-summary
# develop in parallel, push branches, merge on integration branch
git worktree remove ../wt-a
```

See `exercises/a2-worktrees/README.md` for execution notes.
