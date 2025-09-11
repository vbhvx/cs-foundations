"""Unit test suite for Lottery Scheduling with Proportional Shares (os_internals)."""
from os_internals.lottery_scheduler import LotteryScheduler

def test_lottery_scheduler_lifecycle():
    obj = LotteryScheduler("test_lottery_scheduler", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_lottery_scheduler"
    assert status["capacity"] == 10

def test_lottery_scheduler_operations():
    obj = LotteryScheduler("test_lottery_scheduler_ops", capacity=5)
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
