"""Unit test suite for CRDT Logoot Sequence Representation (consensus)."""
from consensus.crdt_logoot import CrdtLogoot

def test_crdt_logoot_lifecycle():
    obj = CrdtLogoot("test_crdt_logoot", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_crdt_logoot"
    assert status["capacity"] == 10

def test_crdt_logoot_operations():
    obj = CrdtLogoot("test_crdt_logoot_ops", capacity=5)
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
