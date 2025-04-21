"""Unit test suite for CRDT PN-Counter (Positive-Negative) (consensus)."""
from consensus.crdt_pn_counter import CrdtPnCounter

def test_crdt_pn_counter_lifecycle():
    obj = CrdtPnCounter("test_crdt_pn_counter", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_crdt_pn_counter"
    assert status["capacity"] == 10

def test_crdt_pn_counter_operations():
    obj = CrdtPnCounter("test_crdt_pn_counter_ops", capacity=5)
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
