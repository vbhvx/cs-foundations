"""Unit test suite for Curve25519 Montgomery Point Ladder (crypto)."""
from crypto.curve25519_ladder import Curve25519Ladder

def test_curve25519_ladder_lifecycle():
    obj = Curve25519Ladder("test_curve25519_ladder", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_curve25519_ladder"
    assert status["capacity"] == 10

def test_curve25519_ladder_operations():
    obj = Curve25519Ladder("test_curve25519_ladder_ops", capacity=5)
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
