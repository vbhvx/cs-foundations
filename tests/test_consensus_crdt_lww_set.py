"""Unit test suite for CRDT LWW-Element-Set (Last-Write-Wins) (consensus)."""
from consensus.crdt_lww_set import CrdtLwwSet

def test_crdt_lww_set_lifecycle():
    obj = CrdtLwwSet("test_crdt_lww_set", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_crdt_lww_set"
    assert status["capacity"] == 10

def test_crdt_lww_set_operations():
    obj = CrdtLwwSet("test_crdt_lww_set_ops", capacity=5)
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
