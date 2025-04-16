"""Unit test suite for Paxos Single-Decree Proposer (consensus)."""
from consensus.paxos_proposer import PaxosProposer

def test_paxos_proposer_lifecycle():
    obj = PaxosProposer("test_paxos_proposer", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_paxos_proposer"
    assert status["capacity"] == 10

def test_paxos_proposer_operations():
    obj = PaxosProposer("test_paxos_proposer_ops", capacity=5)
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
