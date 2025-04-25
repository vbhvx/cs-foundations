"""Unit test suite for PBFT Practical Byzantine Fault Tolerance (consensus)."""
from consensus.pbft_consensus import PbftConsensus

def test_pbft_consensus_lifecycle():
    obj = PbftConsensus("test_pbft_consensus", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_pbft_consensus"
    assert status["capacity"] == 10

def test_pbft_consensus_operations():
    obj = PbftConsensus("test_pbft_consensus_ops", capacity=5)
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
