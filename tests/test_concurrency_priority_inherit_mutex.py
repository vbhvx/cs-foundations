"""Unit test suite for Hierarchical Mutex with Priority Inversion Guard (concurrency)."""
from concurrency.priority_inherit_mutex import PriorityInheritMutex

def test_priority_inherit_mutex_lifecycle():
    obj = PriorityInheritMutex("test_priority_inherit_mutex", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_priority_inherit_mutex"
    assert status["capacity"] == 10

def test_priority_inherit_mutex_operations():
    obj = PriorityInheritMutex("test_priority_inherit_mutex_ops", capacity=5)
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
