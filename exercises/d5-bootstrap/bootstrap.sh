#!/usr/bin/env bash
# D5 — Bootstrap script for assessment environment
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
PY="${PYTHON:-python3}"

echo "==> D5 bootstrap: $ROOT"

check_cmd() {
  if command -v "$1" >/dev/null 2>&1; then
    echo "  ok  $1 ($("$2" 2>/dev/null || echo present))"
  else
    echo "  skip $1 (not installed)"
  fi
}

check_cmd python3 "python3 --version"
check_cmd node "node --version"
check_cmd cargo "cargo --version"
check_cmd docker "docker --version"
check_cmd terraform "terraform --version"
check_cmd kubectl "kubectl --version --client"

echo "==> Installing Python deps for core exercises"
for dir in b4-balance-api i4-currency-convert/api i6-bugfix a3-fraud-score/api i3-mini-change; do
  echo "  pip install: exercises/$dir"
  (cd "$ROOT/exercises/$dir" && $PY -m pip install -q -r requirements.txt)
done

echo "==> Building Rust binaries"
(cargo build --quiet --manifest-path "$ROOT/exercises/b6-rust-log-counter/Cargo.toml")
(cargo build --quiet --manifest-path "$ROOT/exercises/a3-fraud-score/scorer/Cargo.toml")

echo "==> Bootstrap complete. Run: ./scripts/verify-all.sh"
