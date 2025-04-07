"""Unit test suite for RSA-PSS Probabilistic Signature Scheme (crypto)."""
from crypto.rsa_pss import RsaPss

def test_rsa_pss_lifecycle():
    obj = RsaPss("test_rsa_pss", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_rsa_pss"
    assert status["capacity"] == 10

def test_rsa_pss_operations():
    obj = RsaPss("test_rsa_pss_ops", capacity=5)
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
