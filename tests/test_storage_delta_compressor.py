"""Unit test suite for Delta-of-Delta Timestamp Compressor (storage)."""
from storage.delta_compressor import DeltaCompressor

def test_delta_compressor_lifecycle():
    obj = DeltaCompressor("test_delta_compressor", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_delta_compressor"
    assert status["capacity"] == 10

def test_delta_compressor_operations():
    obj = DeltaCompressor("test_delta_compressor_ops", capacity=5)
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
