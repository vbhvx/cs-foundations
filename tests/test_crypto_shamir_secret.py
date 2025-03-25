"""Unit test suite for Shamir Secret Sharing (SSSS) (crypto)."""
from crypto.shamir_secret import ShamirSecret

def test_shamir_secret_lifecycle():
    obj = ShamirSecret("test_shamir_secret", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_shamir_secret"
    assert status["capacity"] == 10

def test_shamir_secret_operations():
    obj = ShamirSecret("test_shamir_secret_ops", capacity=5)
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
