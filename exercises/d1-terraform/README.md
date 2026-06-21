# D1 — Terraform (S3 artifact bucket)

Minimal AWS S3 bucket with versioning for assessment artifacts.

## Dry-run verify

Terraform CLI was **not installed** on build host. Validate when available:

```bash
terraform init
terraform validate
terraform plan -var="bucket_name=atul-assessment-artifacts-demo"
```

## Design

- Single bucket, versioning enabled
- Tagged for exercise traceability
- No state backend configured (local state for demo)
