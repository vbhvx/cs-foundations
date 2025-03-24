"""Unit test suite for BLS Multi-Signature Threshold Scheme (crypto)."""
from crypto.bls_threshold import BlsThreshold

def test_bls_threshold_lifecycle():
    obj = BlsThreshold("test_bls_threshold", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_bls_threshold"
    assert status["capacity"] == 10

def test_bls_threshold_operations():
    obj = BlsThreshold("test_bls_threshold_ops", capacity=5)
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
