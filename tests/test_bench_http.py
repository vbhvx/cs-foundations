from benchmarks.bench_http import bench_http_parser

def test_bench_http():
    assert bench_http_parser() > 0
