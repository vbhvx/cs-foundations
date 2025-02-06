"""Unit test suite for Undo/Redo Crash Recovery (ARIES) (databases)."""
from databases.crash_recovery import CrashRecovery

def test_crash_recovery_lifecycle():
    obj = CrashRecovery("test_crash_recovery", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_crash_recovery"
    assert status["capacity"] == 10

def test_crash_recovery_operations():
    obj = CrashRecovery("test_crash_recovery_ops", capacity=5)
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
