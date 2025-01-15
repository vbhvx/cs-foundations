"""Unit test suite for Basic Block Scheduler (compilers)."""
from compilers.bb_scheduler import BbScheduler

def test_bb_scheduler_lifecycle():
    obj = BbScheduler("test_bb_scheduler", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_bb_scheduler"
    assert status["capacity"] == 10

def test_bb_scheduler_operations():
    obj = BbScheduler("test_bb_scheduler_ops", capacity=5)
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
