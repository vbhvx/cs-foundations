"""Unit test suite for Prefix Compressed Key-Value Block (storage)."""
from storage.prefix_compression import PrefixCompression

def test_prefix_compression_lifecycle():
    obj = PrefixCompression("test_prefix_compression", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_prefix_compression"
    assert status["capacity"] == 10

def test_prefix_compression_operations():
    obj = PrefixCompression("test_prefix_compression_ops", capacity=5)
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
