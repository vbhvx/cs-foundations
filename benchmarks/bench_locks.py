"""Benchmark comparing SpinLock vs threading.Lock contention."""
from concurrency.spinlock import SpinLock
import threading, time

def bench_spinlock_contention(threads: int = 4, iterations: int = 500):
    lock = SpinLock()
    counter = 0
    def worker():
        nonlocal counter
        for _ in range(iterations):
            with lock: counter += 1
    th = [threading.Thread(target=worker) for _ in range(threads)]
    t0 = time.perf_counter()
    for t in th: t.start()
    for t in th: t.join()
    return time.perf_counter() - t0
