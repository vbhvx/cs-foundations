"""Unit test suite for Rate Monotonic Scheduling (RMS) Real-Time (os_internals)."""
from os_internals.rms_scheduler import RmsScheduler

def test_rms_scheduler_lifecycle():
    obj = RmsScheduler("test_rms_scheduler", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_rms_scheduler"
    assert status["capacity"] == 10

def test_rms_scheduler_operations():
    obj = RmsScheduler("test_rms_scheduler_ops", capacity=5)
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
