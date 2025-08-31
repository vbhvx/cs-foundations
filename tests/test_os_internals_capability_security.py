"""Unit test suite for Capability-Based Security Token Matrix (os_internals)."""
from os_internals.capability_security import CapabilitySecurity

def test_capability_security_lifecycle():
    obj = CapabilitySecurity("test_capability_security", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_capability_security"
    assert status["capacity"] == 10

def test_capability_security_operations():
    obj = CapabilitySecurity("test_capability_security_ops", capacity=5)
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
