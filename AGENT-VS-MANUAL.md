# Agent vs Manual Attribution

Honest split of what the coding agent produced vs what a human verified.

| Exercise | Agent did | Human / manual did |
|----------|-----------|-------------------|
| B1–B3, I1, I2 | Drafted analysis from OSS clone | Spot-checked file paths against repo |
| B4–B6 | Implemented APIs/CLI + tests | Re-ran pytest/npm/cargo |
| I3 | Pagination feature + tests | Confirmed fork link still valid |
| I4 | API + CLI | Manual curl/CLI smoke |
| I5, D2 | Docker configs | **Blocked** — no Docker on build machine |
| I6 | Identified discount bug, fixed | Wrote failing test first |
| A1, A2 | Plan + branch strategy docs | Prior worktree run in separate repo |
| A3 | Polyglot pipeline | Three-terminal smoke optional |
| A4 | Modernization refactor | pytest confirmation |
| A5 | Review findings table | — |
| A6 | Bench script | Ran bench, recorded speedup |
| D1, D4 | IaC/manifests | **Blocked** — terraform/kubectl absent |
| D3 | GitHub Actions YAML | Validates on push when published |
| D5 | Bootstrap script | Ran locally |
| D6 | Prometheus/alerts YAML | Config review only |

## Policy

- No code copied from intern repos (`Intern-cohort-main`, `Repo-Analyser-main`, etc.)
- OSS analysis target: `ptrstn/fastapi-sqlalchemy-pytest-example` — fresh writeups, not copied from `Analyzing-tasks`
- Existing Atul repos used as **reference only** for exercise scope
