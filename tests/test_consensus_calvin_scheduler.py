"""Unit test suite for Calvin Deterministic Transaction Scheduler (consensus)."""
from consensus.calvin_scheduler import CalvinScheduler

def test_calvin_scheduler_lifecycle():
    obj = CalvinScheduler("test_calvin_scheduler", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_calvin_scheduler"
    assert status["capacity"] == 10

def test_calvin_scheduler_operations():
    obj = CalvinScheduler("test_calvin_scheduler_ops", capacity=5)
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
