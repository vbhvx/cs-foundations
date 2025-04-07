"""Unit test suite for Ring Signature Anonymity Scheme (crypto)."""
from crypto.ring_signature import RingSignature

def test_ring_signature_lifecycle():
    obj = RingSignature("test_ring_signature", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_ring_signature"
    assert status["capacity"] == 10

def test_ring_signature_operations():
    obj = RingSignature("test_ring_signature_ops", capacity=5)
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
