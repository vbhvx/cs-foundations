from benchmarks.bench_sstable import bench_sstable_lookup

def test_bench_sstable():
    assert bench_sstable_lookup()
