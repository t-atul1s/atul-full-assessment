# Tooling & Verification Notes

This assessment used a coding agent alongside manual review. The table below records what was implemented versus what was independently verified on the build machine.

| Exercise | Implementation | Verification |
|----------|----------------|--------------|
| B1–B3, I1, I2 | OSS repo analysis writeups | File paths and claims checked against upstream source |
| B4–B6 | APIs/CLI + automated tests | pytest, npm test, cargo test |
| I3 | Pagination feature + tests | pytest; fork link validated |
| I4 | API + CLI | pytest + CLI smoke |
| I5, D2 | Docker configs | **Blocked** — Docker not installed on build machine |
| I6 | Discount bug fix + tests | pytest; edge cases spot-checked |
| A1, A2 | Parallel plan + branch strategy | Worktree execution documented in balance-api repo |
| A3 | Polyglot ingest/score pipeline | pytest + cargo test; optional end-to-end curl |
| A4 | Modernization refactor | pytest |
| A5 | Code review findings | Reviewed B4 implementation |
| A6 | Benchmark script | Local bench run recorded in VERIFY-OUTPUT |
| D1, D4 | IaC/manifests | **Blocked** — terraform/kubectl not installed |
| D3 | GitHub Actions workflow | CI runs on push; local verify-all.sh |
| D5 | Bootstrap script | Ran locally |
| D6 | Prometheus/alerts YAML | Config review |

## Notes

- OSS analysis target: [ptrstn/fastapi-sqlalchemy-pytest-example](https://github.com/ptrstn/fastapi-sqlalchemy-pytest-example) @ `19047d7`
- All exercise code in this repo was written for the assessment scope
- Standalone repos listed in README are prior milestones, not substitutes for this submission
