"""Unit test suite for Frame-of-Reference (FoR) Compression (storage)."""
from storage.for_compression import ForCompression

def test_for_compression_lifecycle():
    obj = ForCompression("test_for_compression", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_for_compression"
    assert status["capacity"] == 10

def test_for_compression_operations():
    obj = ForCompression("test_for_compression_ops", capacity=5)
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
