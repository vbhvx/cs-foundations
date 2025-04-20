"""Unit test suite for Chandy-Lamport Global State Snapshot (consensus)."""
from consensus.chandy_lamport import ChandyLamport

def test_chandy_lamport_lifecycle():
    obj = ChandyLamport("test_chandy_lamport", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_chandy_lamport"
    assert status["capacity"] == 10

def test_chandy_lamport_operations():
    obj = ChandyLamport("test_chandy_lamport_ops", capacity=5)
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
