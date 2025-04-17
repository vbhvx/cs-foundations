"""Unit test suite for Raft Log Replication Engine (consensus)."""
from consensus.raft_replication import RaftReplication

def test_raft_replication_lifecycle():
    obj = RaftReplication("test_raft_replication", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_raft_replication"
    assert status["capacity"] == 10

def test_raft_replication_operations():
    obj = RaftReplication("test_raft_replication_ops", capacity=5)
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
