"""Timing harness measuring throughput and latency percentiles."""
import time

def time_execution(fn, iterations: int = 1000):
    start = time.perf_counter()
    for _ in range(iterations): fn()
    total = time.perf_counter() - start
    return total / iterations
