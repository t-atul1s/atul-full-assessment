# I5 — Dockerized Balance API

Wraps the B4 FastAPI service in Docker.

## Verify (requires Docker)

```bash
docker compose up --build -d
curl -X POST localhost:8080/transactions -H 'Content-Type: application/json' -d '{"kind":"credit","amount":10}'
curl localhost:8080/balance
docker compose down
```

## Dry-run (no Docker on build machine)

Docker was **not available** on the submission build host. Config validated by inspection:

- Multi-stage not required; slim Python base
- Healthcheck hits `/balance`
- Port mapping `8080:8000`

See root README **Blockers** section.
