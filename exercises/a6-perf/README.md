# A6 — Performance Profiling

Compares O(n) loop vs closed-form formula for sum of squares.

## Verify

```bash
python3 bench.py
```

Sample output (machine-dependent):

```
n=200000
naive=0.045000s fast=0.000001s speedup=45000.0x
```

## Method

- `time.perf_counter()` over 5 iterations
- Correctness check: both functions agree for n=100
