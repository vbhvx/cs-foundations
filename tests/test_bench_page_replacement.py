from benchmarks.bench_page_replacement import compare_page_algorithms

def test_bench_page():
    res = compare_page_algorithms()
    assert "fifo" in res and "lru" in res
