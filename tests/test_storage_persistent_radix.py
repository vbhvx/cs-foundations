"""Unit test suite for Persistent Radix Tree with Path Compression (storage)."""
from storage.persistent_radix import PersistentRadix

def test_persistent_radix_lifecycle():
    obj = PersistentRadix("test_persistent_radix", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_persistent_radix"
    assert status["capacity"] == 10

def test_persistent_radix_operations():
    obj = PersistentRadix("test_persistent_radix_ops", capacity=5)
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
