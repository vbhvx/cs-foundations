"""Unit test suite for Poly1305 Message Authentication Code (crypto)."""
from crypto.poly1305_mac import Poly1305Mac

def test_poly1305_mac_lifecycle():
    obj = Poly1305Mac("test_poly1305_mac", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_poly1305_mac"
    assert status["capacity"] == 10

def test_poly1305_mac_operations():
    obj = Poly1305Mac("test_poly1305_mac_ops", capacity=5)
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
