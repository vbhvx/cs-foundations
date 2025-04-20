"""Unit test suite for Ring Leader Election Algorithm (consensus)."""
from consensus.ring_election import RingElection

def test_ring_election_lifecycle():
    obj = RingElection("test_ring_election", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_ring_election"
    assert status["capacity"] == 10

def test_ring_election_operations():
    obj = RingElection("test_ring_election_ops", capacity=5)
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
