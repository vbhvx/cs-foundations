"""Unit test suite for HotStuff Pipelined BFT Consensus (consensus)."""
from consensus.hotstuff_bft import HotstuffBft

def test_hotstuff_bft_lifecycle():
    obj = HotstuffBft("test_hotstuff_bft", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_hotstuff_bft"
    assert status["capacity"] == 10

def test_hotstuff_bft_operations():
    obj = HotstuffBft("test_hotstuff_bft_ops", capacity=5)
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
