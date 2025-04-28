"""Unit test suite for Chubby Distributed Lock Client (consensus)."""
from consensus.chubby_lock import ChubbyLock

def test_chubby_lock_lifecycle():
    obj = ChubbyLock("test_chubby_lock", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_chubby_lock"
    assert status["capacity"] == 10

def test_chubby_lock_operations():
    obj = ChubbyLock("test_chubby_lock_ops", capacity=5)
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
