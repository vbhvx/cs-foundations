"""Unit test suite for Sequential Lock (Seqlock) (concurrency)."""
from concurrency.seqlock import Seqlock

def test_seqlock_lifecycle():
    obj = Seqlock("test_seqlock", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_seqlock"
    assert status["capacity"] == 10

def test_seqlock_operations():
    obj = Seqlock("test_seqlock_ops", capacity=5)
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
