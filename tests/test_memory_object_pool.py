"""Unit test suite for Object Pool Lifecycle Manager (memory)."""
from memory.object_pool import ObjectPool

def test_object_pool_lifecycle():
    obj = ObjectPool("test_object_pool", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_object_pool"
    assert status["capacity"] == 10

def test_object_pool_operations():
    obj = ObjectPool("test_object_pool_ops", capacity=5)
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
