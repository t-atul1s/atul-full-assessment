#!/usr/bin/env bash
# Verify all testable exercises in the monorepo
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PY="${PYTHON:-python3}"
PASS=0
FAIL=0
SKIP=0
BLOCKED=0

green() { printf '\033[32m%s\033[0m\n' "$1"; }
red() { printf '\033[31m%s\033[0m\n' "$1"; }
yellow() { printf '\033[33m%s\033[0m\n' "$1"; }

run_pytest() {
  local name="$1" dir="$2"
  echo "==> $name"
  if (cd "$dir" && $PY -m pip install -q -r requirements.txt && $PY -m pytest -q); then
    green "PASS $name"
    PASS=$((PASS + 1))
  else
    red "FAIL $name"
    FAIL=$((FAIL + 1))
  fi
}

run_node() {
  local name="$1" dir="$2"
  echo "==> $name"
  if (cd "$dir" && npm test); then
    green "PASS $name"
    PASS=$((PASS + 1))
  else
    red "FAIL $name"
    FAIL=$((FAIL + 1))
  fi
}

run_cargo() {
  local name="$1" dir="$2"
  echo "==> $name"
  if (cd "$dir" && cargo test -q); then
    green "PASS $name"
    PASS=$((PASS + 1))
  else
    red "FAIL $name"
    FAIL=$((FAIL + 1))
  fi
}

run_cmd() {
  local name="$1"
  shift
  echo "==> $name"
  if "$@"; then
    green "PASS $name"
    PASS=$((PASS + 1))
  else
    red "FAIL $name"
    FAIL=$((FAIL + 1))
  fi
}

check_blocked() {
  local name="$1" cmd="$2"
  echo "==> $name"
  if command -v "$cmd" >/dev/null 2>&1; then
    yellow "AVAILABLE $name ($cmd found — run exercise README for full verify)"
    SKIP=$((SKIP + 1))
  else
    yellow "BLOCKED $name ($cmd not installed — config-only dry-run)"
    BLOCKED=$((BLOCKED + 1))
  fi
}

cd "$ROOT"

run_pytest "B4 balance API" "exercises/b4-balance-api"
run_node "B5 node balance API" "exercises/b5-node-balance-api"
run_cargo "B6 rust log counter" "exercises/b6-rust-log-counter"
run_pytest "I4 currency API" "exercises/i4-currency-convert/api"
run_pytest "I6 bugfix" "exercises/i6-bugfix"
run_pytest "I3 mini change" "exercises/i3-mini-change"
run_pytest "A3 fraud ingest API" "exercises/a3-fraud-score/api"
run_cargo "A3 fraud scorer" "exercises/a3-fraud-score/scorer"
run_cmd "A4 modernization" bash -c "cd exercises/a4-modernization && $PY -m pip install -q -r requirements.txt && PYTHONPATH=modernized $PY -m pytest -q tests/"
run_cmd "A6 perf bench" bash -c "cd exercises/a6-perf && $PY bench.py"

check_blocked "I5 dockerized API" docker
check_blocked "D1 terraform" terraform
check_blocked "D2 docker compose stack" docker
check_blocked "D4 k8s manifests" kubectl

echo ""
echo "Summary: pass=$PASS fail=$FAIL skip=$SKIP blocked=$BLOCKED"
if [[ $FAIL -gt 0 ]]; then exit 1; fi
