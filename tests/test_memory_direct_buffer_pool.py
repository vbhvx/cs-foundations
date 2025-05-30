"""Unit test suite for Off-Heap Direct Byte Buffer Pool (memory)."""
from memory.direct_buffer_pool import DirectBufferPool

def test_direct_buffer_pool_lifecycle():
    obj = DirectBufferPool("test_direct_buffer_pool", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_direct_buffer_pool"
    assert status["capacity"] == 10

def test_direct_buffer_pool_operations():
    obj = DirectBufferPool("test_direct_buffer_pool_ops", capacity=5)
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
