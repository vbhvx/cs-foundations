"""Unit test suite for CyclicBarrier Reusable Sync Point (concurrency)."""
from concurrency.cyclic_barrier import CyclicBarrier

def test_cyclic_barrier_lifecycle():
    obj = CyclicBarrier("test_cyclic_barrier", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_cyclic_barrier"
    assert status["capacity"] == 10

def test_cyclic_barrier_operations():
    obj = CyclicBarrier("test_cyclic_barrier_ops", capacity=5)
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
