"""Unit test suite for Memory Pool Cache (memory)."""
from memory.memory_pool import MemoryPool

def test_memory_pool_lifecycle():
    obj = MemoryPool("test_memory_pool", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_memory_pool"
    assert status["capacity"] == 10

def test_memory_pool_operations():
    obj = MemoryPool("test_memory_pool_ops", capacity=5)
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
