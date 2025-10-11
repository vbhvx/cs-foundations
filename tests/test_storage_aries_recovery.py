"""Unit test suite for WAL ARIES Redo-Undo Recovery Manager (storage)."""
from storage.aries_recovery import AriesRecovery

def test_aries_recovery_lifecycle():
    obj = AriesRecovery("test_aries_recovery", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_aries_recovery"
    assert status["capacity"] == 10

def test_aries_recovery_operations():
    obj = AriesRecovery("test_aries_recovery_ops", capacity=5)
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
