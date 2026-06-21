"""A6 — naive vs optimized aggregation for perf comparison."""
import random
import time


def sum_squares_naive(n: int) -> int:
    total = 0
    for i in range(n):
        total += i * i
    return total


def sum_squares_fast(n: int) -> int:
    # sum(i^2 for i in 0..n-1) = (n-1)*n*(2n-1)/6
    m = n - 1
    return m * n * (2 * m + 1) // 6


def bench(fn, n: int, repeats: int = 5) -> float:
    random.seed(0)
    start = time.perf_counter()
    for _ in range(repeats):
        fn(n)
    return (time.perf_counter() - start) / repeats


if __name__ == "__main__":
    N = 200_000
    t_slow = bench(sum_squares_naive, N)
    t_fast = bench(sum_squares_fast, N)
    ratio = t_slow / t_fast if t_fast else float("inf")
    print(f"n={N}")
    print(f"naive={t_slow:.6f}s fast={t_fast:.6f}s speedup={ratio:.1f}x")
    assert sum_squares_naive(100) == sum_squares_fast(100)
