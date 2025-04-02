"""Unit test suite for SipHash Fast Short-Input Keyed Hash (crypto)."""
from crypto.siphash import Siphash

def test_siphash_lifecycle():
    obj = Siphash("test_siphash", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_siphash"
    assert status["capacity"] == 10

def test_siphash_operations():
    obj = Siphash("test_siphash_ops", capacity=5)
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
