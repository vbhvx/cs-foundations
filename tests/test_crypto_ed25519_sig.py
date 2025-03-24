"""Unit test suite for Ed25519 Twisted Edwards Signature (crypto)."""
from crypto.ed25519_sig import Ed25519Sig

def test_ed25519_sig_lifecycle():
    obj = Ed25519Sig("test_ed25519_sig", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_ed25519_sig"
    assert status["capacity"] == 10

def test_ed25519_sig_operations():
    obj = Ed25519Sig("test_ed25519_sig_ops", capacity=5)
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
