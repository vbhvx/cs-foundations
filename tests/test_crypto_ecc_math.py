"""Unit test suite for Elliptic Curve Point Arithmetic (crypto)."""
from crypto.ecc_math import EccMath

def test_ecc_math_lifecycle():
    obj = EccMath("test_ecc_math", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_ecc_math"
    assert status["capacity"] == 10

def test_ecc_math_operations():
    obj = EccMath("test_ecc_math_ops", capacity=5)
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
