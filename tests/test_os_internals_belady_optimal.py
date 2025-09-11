"""Unit test suite for Optimal Page Replacement (Belady's MIN) (os_internals)."""
from os_internals.belady_optimal import BeladyOptimal

def test_belady_optimal_lifecycle():
    obj = BeladyOptimal("test_belady_optimal", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_belady_optimal"
    assert status["capacity"] == 10

def test_belady_optimal_operations():
    obj = BeladyOptimal("test_belady_optimal_ops", capacity=5)
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
