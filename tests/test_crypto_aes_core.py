"""Unit test suite for AES-128 Block Cipher Core (crypto)."""
from crypto.aes_core import AesCore

def test_aes_core_lifecycle():
    obj = AesCore("test_aes_core", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_aes_core"
    assert status["capacity"] == 10

def test_aes_core_operations():
    obj = AesCore("test_aes_core_ops", capacity=5)
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
