"""Unit test suite for Diffie-Hellman Key Exchange (crypto)."""
from crypto.diffie_hellman import DiffieHellman

def test_diffie_hellman_lifecycle():
    obj = DiffieHellman("test_diffie_hellman", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_diffie_hellman"
    assert status["capacity"] == 10

def test_diffie_hellman_operations():
    obj = DiffieHellman("test_diffie_hellman_ops", capacity=5)
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
