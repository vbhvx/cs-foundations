"""Unit test suite for Read-Copy-Update (RCU) Epoch Manager (concurrency)."""
from concurrency.rcu_manager import RcuManager

def test_rcu_manager_lifecycle():
    obj = RcuManager("test_rcu_manager", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_rcu_manager"
    assert status["capacity"] == 10

def test_rcu_manager_operations():
    obj = RcuManager("test_rcu_manager_ops", capacity=5)
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
