"""Unit test suite for Completely Fair Scheduler (CFS) (os_internals)."""
from os_internals.cfs_scheduler import CfsScheduler

def test_cfs_scheduler_lifecycle():
    obj = CfsScheduler("test_cfs_scheduler", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_cfs_scheduler"
    assert status["capacity"] == 10

def test_cfs_scheduler_operations():
    obj = CfsScheduler("test_cfs_scheduler_ops", capacity=5)
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
