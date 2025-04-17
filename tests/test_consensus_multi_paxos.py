"""Unit test suite for Paxos Multi-Decree Log Manager (consensus)."""
from consensus.multi_paxos import MultiPaxos

def test_multi_paxos_lifecycle():
    obj = MultiPaxos("test_multi_paxos", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_multi_paxos"
    assert status["capacity"] == 10

def test_multi_paxos_operations():
    obj = MultiPaxos("test_multi_paxos_ops", capacity=5)
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
