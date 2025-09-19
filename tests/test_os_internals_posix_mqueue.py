"""Unit test suite for POSIX Message Queue with Priority Order (os_internals)."""
from os_internals.posix_mqueue import PosixMqueue

def test_posix_mqueue_lifecycle():
    obj = PosixMqueue("test_posix_mqueue", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_posix_mqueue"
    assert status["capacity"] == 10

def test_posix_mqueue_operations():
    obj = PosixMqueue("test_posix_mqueue_ops", capacity=5)
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
