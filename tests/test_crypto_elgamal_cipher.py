"""Unit test suite for ElGamal Discrete Logarithm Encryption (crypto)."""
from crypto.elgamal_cipher import ElgamalCipher

def test_elgamal_cipher_lifecycle():
    obj = ElgamalCipher("test_elgamal_cipher", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_elgamal_cipher"
    assert status["capacity"] == 10

def test_elgamal_cipher_operations():
    obj = ElgamalCipher("test_elgamal_cipher_ops", capacity=5)
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
