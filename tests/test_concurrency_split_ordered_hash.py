"""Unit test suite for Lock-Free Hash Table with Split-Ordered Lists (concurrency)."""
from concurrency.split_ordered_hash import SplitOrderedHash

def test_split_ordered_hash_lifecycle():
    obj = SplitOrderedHash("test_split_ordered_hash", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_split_ordered_hash"
    assert status["capacity"] == 10

def test_split_ordered_hash_operations():
    obj = SplitOrderedHash("test_split_ordered_hash_ops", capacity=5)
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
