"""Unit test suite for AES Galois Counter Mode (GCM) (crypto)."""
from crypto.aes_gcm import AesGcm

def test_aes_gcm_lifecycle():
    obj = AesGcm("test_aes_gcm", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_aes_gcm"
    assert status["capacity"] == 10

def test_aes_gcm_operations():
    obj = AesGcm("test_aes_gcm_ops", capacity=5)
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
