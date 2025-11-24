"""Unit test suite for Tapestry Decentralized Distributed Routing (distributed)."""
from distributed.tapestry_p2p import TapestryP2p

def test_tapestry_p2p_lifecycle():
    obj = TapestryP2p("test_tapestry_p2p", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_tapestry_p2p"
    assert status["capacity"] == 10

def test_tapestry_p2p_operations():
    obj = TapestryP2p("test_tapestry_p2p_ops", capacity=5)
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
