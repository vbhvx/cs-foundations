"""Unit test suite for Priority Task Work-Stealing Stealer (concurrency)."""
from concurrency.priority_work_steal import PriorityWorkSteal

def test_priority_work_steal_lifecycle():
    obj = PriorityWorkSteal("test_priority_work_steal", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_priority_work_steal"
    assert status["capacity"] == 10

def test_priority_work_steal_operations():
    obj = PriorityWorkSteal("test_priority_work_steal_ops", capacity=5)
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
