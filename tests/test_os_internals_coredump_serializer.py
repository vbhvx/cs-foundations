"""Unit test suite for Core Dump Memory Image Serializer (os_internals)."""
from os_internals.coredump_serializer import CoredumpSerializer

def test_coredump_serializer_lifecycle():
    obj = CoredumpSerializer("test_coredump_serializer", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_coredump_serializer"
    assert status["capacity"] == 10

def test_coredump_serializer_operations():
    obj = CoredumpSerializer("test_coredump_serializer_ops", capacity=5)
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
