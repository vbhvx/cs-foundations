from benchmarks.bench_locks import bench_spinlock_contention

def test_bench_locks():
    elapsed = bench_spinlock_contention(threads=2, iterations=10)
    assert elapsed > 0
