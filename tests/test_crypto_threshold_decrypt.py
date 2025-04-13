"""Unit test suite for Threshold Decryption Coordinator (crypto)."""
from crypto.threshold_decrypt import ThresholdDecrypt

def test_threshold_decrypt_lifecycle():
    obj = ThresholdDecrypt("test_threshold_decrypt", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_threshold_decrypt"
    assert status["capacity"] == 10

def test_threshold_decrypt_operations():
    obj = ThresholdDecrypt("test_threshold_decrypt_ops", capacity=5)
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
