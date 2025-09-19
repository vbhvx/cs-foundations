"""Unit test suite for Futex Fast Userspace Mutex Primitive (os_internals)."""
from os_internals.futex_primitive import FutexPrimitive

def test_futex_primitive_lifecycle():
    obj = FutexPrimitive("test_futex_primitive", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_futex_primitive"
    assert status["capacity"] == 10

def test_futex_primitive_operations():
    obj = FutexPrimitive("test_futex_primitive_ops", capacity=5)
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
