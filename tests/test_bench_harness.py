from benchmarks.harness import time_execution

def test_harness():
    avg = time_execution(lambda: sum(range(10)), 100)
    assert avg > 0
