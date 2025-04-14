"""Unit test suite for Homomorphic Paillier Encryption (crypto)."""
from crypto.paillier_crypto import PaillierCrypto

def test_paillier_crypto_lifecycle():
    obj = PaillierCrypto("test_paillier_crypto", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_paillier_crypto"
    assert status["capacity"] == 10

def test_paillier_crypto_operations():
    obj = PaillierCrypto("test_paillier_crypto_ops", capacity=5)
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
