"""Unit test suite for Quorum Lease Heartbeat Renewal (consensus)."""
from consensus.quorum_lease import QuorumLease

def test_quorum_lease_lifecycle():
    obj = QuorumLease("test_quorum_lease", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_quorum_lease"
    assert status["capacity"] == 10

def test_quorum_lease_operations():
    obj = QuorumLease("test_quorum_lease_ops", capacity=5)
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
