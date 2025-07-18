"""Unit test suite for ICE Candidate Gathering & Connectivity (networking)."""
from networking.ice_connectivity import IceConnectivity

def test_ice_connectivity_lifecycle():
    obj = IceConnectivity("test_ice_connectivity", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_ice_connectivity"
    assert status["capacity"] == 10

def test_ice_connectivity_operations():
    obj = IceConnectivity("test_ice_connectivity_ops", capacity=5)
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
