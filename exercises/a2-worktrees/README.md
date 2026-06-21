# A2 — Worktree Execution Notes

This monorepo documents the A1 parallel plan. Feature branches are described here; full git worktree history is in the separate [balance-api](https://github.com/t-atul1s/balance-api) repo.

## Simulated integration outcome

After merging both lanes into B4, the API would expose:

| Endpoint | Source lane |
|----------|-------------|
| GET `/transactions/{id}` | Lane A |
| GET `/summary` | Lane B |

## In-monorepo proof

The B4 baseline in `exercises/b4-balance-api/` is the merge base. For a live worktree demo, run:

```bash
cd exercises/b4-balance-api
git init  # local only
git checkout -b exercise/a2-worktrees
# apply lane patches manually or cherry-pick from balance-api repo
pytest tests/ -v
```

## Reference (external)

Prior execution with real worktrees: https://github.com/t-atul1s/balance-api/tree/exercise/a2-worktrees

## Evidence checklist

- [x] A1 plan document (`docs/a1-parallel-plan.md`)
- [x] Branch naming convention documented
- [x] Merge order + conflict strategy
- [ ] Live worktree logs (see external repo)

## Execution notes

Worktree commands were run in the `balance-api` repo to avoid nested git complexity in this monorepo. See the external link above for branch history and merge evidence.
