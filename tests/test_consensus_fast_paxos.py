"""Unit test suite for Fast Paxos Leaderless Quorum (consensus)."""
from consensus.fast_paxos import FastPaxos

def test_fast_paxos_lifecycle():
    obj = FastPaxos("test_fast_paxos", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_fast_paxos"
    assert status["capacity"] == 10

def test_fast_paxos_operations():
    obj = FastPaxos("test_fast_paxos_ops", capacity=5)
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
