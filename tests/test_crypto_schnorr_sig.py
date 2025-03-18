"""Unit test suite for Schnorr Signature Aggregation (crypto)."""
from crypto.schnorr_sig import SchnorrSig

def test_schnorr_sig_lifecycle():
    obj = SchnorrSig("test_schnorr_sig", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_schnorr_sig"
    assert status["capacity"] == 10

def test_schnorr_sig_operations():
    obj = SchnorrSig("test_schnorr_sig_ops", capacity=5)
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
