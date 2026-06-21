# D6 — Observability

Prometheus scrape config + sample alert rule for balance API availability.

## Components

| File | Purpose |
|------|---------|
| `prometheus.yml` | Scrape jobs |
| `alerts.yml` | `BalanceApiDown` alert |

## Verify

Requires Prometheus + running API. Dry-run: review config syntax (valid YAML).

```bash
# When prometheus image available:
# docker run --rm -v "$PWD/prometheus.yml:/etc/prometheus/prometheus.yml" prom/prometheus --config.file=/etc/prometheus/prometheus.yml --help
```
