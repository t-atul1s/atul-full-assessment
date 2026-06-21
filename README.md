# Coding Agent Assessment — Atul (Complete Monorepo)

**Candidate:** Atul · **Employee ID:** T4538 · **Email:** t-atul1.s@pmltp.com

![CI](https://github.com/t-atul1s/atul-full-assessment/actions/workflows/ci.yml/badge.svg)

Single monorepo covering **all 24 assessment exercises** (B1–B6, I1–I6, A1–A6, D1–D6) with original code, OSS analysis docs, and one-command verification.

---

## Quick start

```bash
cd atul-full-assessment
make verify          # runs scripts/verify-all.sh
# or
./scripts/verify-all.sh
```

Optional bootstrap (install deps + build Rust):

```bash
./exercises/d5-bootstrap/bootstrap.sh
```

---

## Exercise matrix

| ID | Title | Status | Path | Verify |
|----|-------|--------|------|--------|
| **B1** | Repo inventory | Done | [docs/b1-repo-inventory.md](docs/b1-repo-inventory.md) | Read doc |
| **B2** | API endpoint map | Done | [docs/b2-api-map.md](docs/b2-api-map.md) | Read doc |
| **B3** | Test discovery | Done | [docs/b3-test-discovery.md](docs/b3-test-discovery.md) | Read doc |
| **B4** | FastAPI balance API | Done | [exercises/b4-balance-api/](exercises/b4-balance-api/) | `pytest tests/ -v` |
| **B5** | Node balance API | Done | [exercises/b5-node-balance-api/](exercises/b5-node-balance-api/) | `npm test` |
| **B6** | Rust log counter CLI | Done | [exercises/b6-rust-log-counter/](exercises/b6-rust-log-counter/) | `cargo test` |
| **I1** | ER diagram | Done | [docs/i1-er-diagram.md](docs/i1-er-diagram.md) | Read doc |
| **I2** | Flow trace | Done | [docs/i2-flow-trace.md](docs/i2-flow-trace.md) | Read doc |
| **I3** | Small OSS change | Done | [exercises/i3-mini-change/](exercises/i3-mini-change/) + [i3-fork-notes.md](i3-fork-notes.md) | `pytest tests/ -v` |
| **I4** | Currency convert pair | Done | [exercises/i4-currency-convert/](exercises/i4-currency-convert/) | `pytest` + `node cli.js` |
| **I5** | Dockerized API | Config | [exercises/i5-dockerized-api/](exercises/i5-dockerized-api/) | `docker compose up` *(blocked)* |
| **I6** | Bug fix | Done | [exercises/i6-bugfix/](exercises/i6-bugfix/) | `pytest tests/ -v` |
| **A1** | Parallel plan | Done | [docs/a1-parallel-plan.md](docs/a1-parallel-plan.md) | Read doc |
| **A2** | Worktrees | Done | [exercises/a2-worktrees/](exercises/a2-worktrees/) | See README |
| **A3** | Fraud score polyglot | Done | [exercises/a3-fraud-score/](exercises/a3-fraud-score/) | `pytest` + `cargo test` |
| **A4** | Modernization | Done | [exercises/a4-modernization/](exercises/a4-modernization/) | `PYTHONPATH=modernized pytest` |
| **A5** | Code review | Done | [docs/a5-code-review.md](docs/a5-code-review.md) | Read doc |
| **A6** | Perf profiling | Done | [exercises/a6-perf/](exercises/a6-perf/) | `python3 bench.py` |
| **D1** | Terraform | Config | [exercises/d1-terraform/](exercises/d1-terraform/) | `terraform validate` *(blocked)* |
| **D2** | Docker compose stack | Config | [exercises/d2-docker-compose/](exercises/d2-docker-compose/) | `docker compose up` *(blocked)* |
| **D3** | CI pipeline | Done | [.github/workflows/ci.yml](.github/workflows/ci.yml) | `./scripts/verify-all.sh` |
| **D4** | K8s manifests | Config | [exercises/d4-k8s/](exercises/d4-k8s/) | `kubectl apply --dry-run=client` *(blocked)* |
| **D5** | Bootstrap script | Done | [exercises/d5-bootstrap/](exercises/d5-bootstrap/) | `./bootstrap.sh` |
| **D6** | Observability | Config | [exercises/d6-observability/](exercises/d6-observability/) | Review YAML |

**Legend:** Done = runnable/tests pass · Config = valid artifacts, runtime tool missing on build host

---

## OSS analysis target

All read exercises analyze: [ptrstn/fastapi-sqlalchemy-pytest-example](https://github.com/ptrstn/fastapi-sqlalchemy-pytest-example) @ commit `19047d7`.

Local clone (if present): `~/Desktop/repos/fastapi-sqlalchemy-pytest-example`

---

## Repository layout

```
atul-full-assessment/
├── README.md                 # This file
├── Makefile                  # make verify
├── VERIFY.md                 # Verification guide
├── AGENT-VS-MANUAL.md        # Tooling and verification notes
├── i3-fork-notes.md
├── docs/                     # B1,B2,B3,I1,I2,A1,A5 + screenshots
├── scripts/verify-all.sh
├── exercises/                # All build/DevOps exercises
└── .github/workflows/ci.yml
```

---

## Blockers (build machine)

| Tool | Affects | Unblock |
|------|---------|---------|
| Docker | I5, D2 | Install Docker Desktop; run `docker compose up` |
| Terraform | D1 | `brew install terraform && terraform validate` |
| kubectl | D4 | `brew install kubectl` + dry-run apply |

Configs are valid and ready — see per-exercise READMEs.

---

## Related repositories

Standalone repos from earlier milestones remain available for cross-reference:

- [balance-api](https://github.com/t-atul1s/balance-api)
- [Analyzing-tasks](https://github.com/t-atul1s/Analyzing-tasks)
- [fraud-score-system](https://github.com/t-atul1s/fraud-score-system)
- [currency-convert](https://github.com/t-atul1s/currency-convert)

---

## Related docs

- [VERIFY.md](VERIFY.md) — per-exercise verify commands
- [VERIFY-OUTPUT.md](VERIFY-OUTPUT.md) — last test run output
- [AGENT-VS-MANUAL.md](AGENT-VS-MANUAL.md) — tooling and verification notes
- [docs/screenshots/](docs/screenshots/) — API smoke-test captures
