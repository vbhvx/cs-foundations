"""Unit test suite for RSA Public Key Encryption (crypto)."""
from crypto.rsa_cipher import RsaCipher

def test_rsa_cipher_lifecycle():
    obj = RsaCipher("test_rsa_cipher", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_rsa_cipher"
    assert status["capacity"] == 10

def test_rsa_cipher_operations():
    obj = RsaCipher("test_rsa_cipher_ops", capacity=5)
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
