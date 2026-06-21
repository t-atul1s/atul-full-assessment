# Verification Guide

Run everything:

```bash
make verify
# or
./scripts/verify-all.sh
```

## Per-exercise commands

| Exercise | Command |
|----------|---------|
| B4 | `cd exercises/b4-balance-api && pytest -v` |
| B5 | `cd exercises/b5-node-balance-api && npm test` |
| B6 | `cd exercises/b6-rust-log-counter && cargo test` |
| I4 | `cd exercises/i4-currency-convert/api && pytest -v` |
| I6 | `cd exercises/i6-bugfix && pytest -v` |
| I3 | `cd exercises/i3-mini-change && pytest -v` |
| A3 | `cd exercises/a3-fraud-score/api && pytest -v && cd ../scorer && cargo test` |
| A4 | `cd exercises/a4-modernization && PYTHONPATH=modernized pytest -v` |
| A6 | `cd exercises/a6-perf && python3 bench.py` |
| I5/D2 | `docker compose up` (requires Docker) |
| D1 | `terraform validate` (requires Terraform) |
| D4 | `kubectl apply --dry-run=client -f exercises/d4-k8s/deployment.yaml` |

## Last run output

See `VERIFY-OUTPUT.md` (generated after local verify-all run).
