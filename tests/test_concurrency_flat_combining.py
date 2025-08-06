"""Unit test suite for Flat Combining Concurrent Data Structure (concurrency)."""
from concurrency.flat_combining import FlatCombining

def test_flat_combining_lifecycle():
    obj = FlatCombining("test_flat_combining", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_flat_combining"
    assert status["capacity"] == 10

def test_flat_combining_operations():
    obj = FlatCombining("test_flat_combining_ops", capacity=5)
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
