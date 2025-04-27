"""Unit test suite for Raft Dynamic Cluster Membership Change (consensus)."""
from consensus.raft_membership import RaftMembership

def test_raft_membership_lifecycle():
    obj = RaftMembership("test_raft_membership", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_raft_membership"
    assert status["capacity"] == 10

def test_raft_membership_operations():
    obj = RaftMembership("test_raft_membership_ops", capacity=5)
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
