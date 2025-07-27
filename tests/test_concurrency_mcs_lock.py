"""Unit test suite for Mellor-Crummey and Scott (MCS) Lock (concurrency)."""
from concurrency.mcs_lock import McsLock

def test_mcs_lock_lifecycle():
    obj = McsLock("test_mcs_lock", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_mcs_lock"
    assert status["capacity"] == 10

def test_mcs_lock_operations():
    obj = McsLock("test_mcs_lock_ops", capacity=5)
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
