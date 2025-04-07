"""Unit test suite for Constant-Time Memcmp Security Helper (crypto)."""
from crypto.constant_time_mem import ConstantTimeMem

def test_constant_time_mem_lifecycle():
    obj = ConstantTimeMem("test_constant_time_mem", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_constant_time_mem"
    assert status["capacity"] == 10

def test_constant_time_mem_operations():
    obj = ConstantTimeMem("test_constant_time_mem_ops", capacity=5)
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
