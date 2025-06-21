"""Unit test suite for Garbage Collector Safepoint Barrier (memory)."""
from memory.safepoint_barrier import SafepointBarrier

def test_safepoint_barrier_lifecycle():
    obj = SafepointBarrier("test_safepoint_barrier", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_safepoint_barrier"
    assert status["capacity"] == 10

def test_safepoint_barrier_operations():
    obj = SafepointBarrier("test_safepoint_barrier_ops", capacity=5)
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
