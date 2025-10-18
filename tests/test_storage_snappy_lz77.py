"""Unit test suite for Snappy-Style Fast LZ77 Byte Compressor (storage)."""
from storage.snappy_lz77 import SnappyLz77

def test_snappy_lz77_lifecycle():
    obj = SnappyLz77("test_snappy_lz77", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_snappy_lz77"
    assert status["capacity"] == 10

def test_snappy_lz77_operations():
    obj = SnappyLz77("test_snappy_lz77_ops", capacity=5)
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
