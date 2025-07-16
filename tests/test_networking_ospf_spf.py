"""Unit test suite for OSPF Link-State Dijkstra SPF Engine (networking)."""
from networking.ospf_spf import OspfSpf

def test_ospf_spf_lifecycle():
    obj = OspfSpf("test_ospf_spf", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_ospf_spf"
    assert status["capacity"] == 10

def test_ospf_spf_operations():
    obj = OspfSpf("test_ospf_spf_ops", capacity=5)
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
