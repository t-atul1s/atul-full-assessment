# B6 — Rust Log Counter CLI

Counts log-level tokens (`INFO`, `WARN`, `ERROR`, etc.) in a file or stdin.

## Verify

```bash
cargo test
echo -e "INFO start\nERROR fail\nINFO ok" | cargo run --quiet
```

Expected output:

```
total=3
ERROR=1
INFO=2
```
