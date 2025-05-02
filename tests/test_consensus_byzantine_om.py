"""Unit test suite for Byzantine Generals Oral Message Algorithm (consensus)."""
from consensus.byzantine_om import ByzantineOm

def test_byzantine_om_lifecycle():
    obj = ByzantineOm("test_byzantine_om", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_byzantine_om"
    assert status["capacity"] == 10

def test_byzantine_om_operations():
    obj = ByzantineOm("test_byzantine_om_ops", capacity=5)
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
