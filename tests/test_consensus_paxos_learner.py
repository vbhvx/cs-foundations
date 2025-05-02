"""Unit test suite for Paxos Learner Consensus Broadcast (consensus)."""
from consensus.paxos_learner import PaxosLearner

def test_paxos_learner_lifecycle():
    obj = PaxosLearner("test_paxos_learner", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_paxos_learner"
    assert status["capacity"] == 10

def test_paxos_learner_operations():
    obj = PaxosLearner("test_paxos_learner_ops", capacity=5)
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
