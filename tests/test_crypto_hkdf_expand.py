"""Unit test suite for HKDF Extract-and-Expand Key Derivation (crypto)."""
from crypto.hkdf_expand import HkdfExpand

def test_hkdf_expand_lifecycle():
    obj = HkdfExpand("test_hkdf_expand", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_hkdf_expand"
    assert status["capacity"] == 10

def test_hkdf_expand_operations():
    obj = HkdfExpand("test_hkdf_expand_ops", capacity=5)
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
