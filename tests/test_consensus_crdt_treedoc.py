"""Unit test suite for CRDT Treedoc Collaborative Editor (consensus)."""
from consensus.crdt_treedoc import CrdtTreedoc

def test_crdt_treedoc_lifecycle():
    obj = CrdtTreedoc("test_crdt_treedoc", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_crdt_treedoc"
    assert status["capacity"] == 10

def test_crdt_treedoc_operations():
    obj = CrdtTreedoc("test_crdt_treedoc_ops", capacity=5)
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
