# D4 — Kubernetes Manifests

Deployment + Service for B4 balance API (2 replicas, readiness probe on `/balance`).

## Dry-run verify

```bash
kubectl apply --dry-run=client -f deployment.yaml
```

kubectl was **not installed** on build host.
