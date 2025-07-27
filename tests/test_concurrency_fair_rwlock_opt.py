"""Unit test suite for Fair Read-Write Lock (No Starvation) (concurrency)."""
from concurrency.fair_rwlock_opt import FairRwlockOpt

def test_fair_rwlock_opt_lifecycle():
    obj = FairRwlockOpt("test_fair_rwlock_opt", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_fair_rwlock_opt"
    assert status["capacity"] == 10

def test_fair_rwlock_opt_operations():
    obj = FairRwlockOpt("test_fair_rwlock_opt_ops", capacity=5)
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
