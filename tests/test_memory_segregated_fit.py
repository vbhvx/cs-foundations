"""Unit test suite for Segregated Free List Allocator (memory)."""
from memory.segregated_fit import SegregatedFit

def test_segregated_fit_lifecycle():
    obj = SegregatedFit("test_segregated_fit", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_segregated_fit"
    assert status["capacity"] == 10

def test_segregated_fit_operations():
    obj = SegregatedFit("test_segregated_fit_ops", capacity=5)
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
