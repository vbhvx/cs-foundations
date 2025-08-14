"""Unit test suite for Fork-Join Task Deque Framework (concurrency)."""
from concurrency.fork_join_framework import ForkJoinFramework

def test_fork_join_framework_lifecycle():
    obj = ForkJoinFramework("test_fork_join_framework", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_fork_join_framework"
    assert status["capacity"] == 10

def test_fork_join_framework_operations():
    obj = ForkJoinFramework("test_fork_join_framework_ops", capacity=5)
    ok, res = obj.execute("k1", 100)
    assert ok is True
    assert res == 100
    assert obj.query("k1") == 100
    assert obj.size() == 1
    
    # Overwrite
    ok, res = obj.execute("k1", 200)
    assert ok is True
    assert obj.query("k1") == 200
    assert obj.size() == 1
    
    # Reset
    obj.reset()
    assert obj.size() == 0
