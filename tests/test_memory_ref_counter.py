"""Unit test suite for Reference Counting with Trial Deletion (memory)."""
from memory.ref_counter import RefCounter

def test_ref_counter_lifecycle():
    obj = RefCounter("test_ref_counter", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_ref_counter"
    assert status["capacity"] == 10

def test_ref_counter_operations():
    obj = RefCounter("test_ref_counter_ops", capacity=5)
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
