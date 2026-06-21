# D2 — Docker Compose Stack

Multi-service stack: balance API, currency API, Prometheus scraper config.

## Verify (requires Docker)

```bash
docker compose up --build
curl localhost:8080/balance
curl localhost:8081/health
```

## Blocker

Docker not available on submission build host — configs provided for reviewer dry-run.
