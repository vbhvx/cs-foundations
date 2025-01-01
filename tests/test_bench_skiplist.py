from benchmarks.bench_skiplist import bench_skiplist_insert

def test_bench_skiplist():
    assert bench_skiplist_insert() > 0
