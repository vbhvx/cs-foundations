"""Unit test suite for Bully Leader Election Algorithm (consensus)."""
from consensus.bully_election import BullyElection

def test_bully_election_lifecycle():
    obj = BullyElection("test_bully_election", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_bully_election"
    assert status["capacity"] == 10

def test_bully_election_operations():
    obj = BullyElection("test_bully_election_ops", capacity=5)
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
