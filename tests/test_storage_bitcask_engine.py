"""Unit test suite for Persistent Hash Index (Bitcask Architecture) (storage)."""
from storage.bitcask_engine import BitcaskEngine

def test_bitcask_engine_lifecycle():
    obj = BitcaskEngine("test_bitcask_engine", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_bitcask_engine"
    assert status["capacity"] == 10

def test_bitcask_engine_operations():
    obj = BitcaskEngine("test_bitcask_engine_ops", capacity=5)
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
