"""Unit test suite for EPaxos Egalitarian Consensus Protocol (consensus)."""
from consensus.epaxos_protocol import EpaxosProtocol

def test_epaxos_protocol_lifecycle():
    obj = EpaxosProtocol("test_epaxos_protocol", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_epaxos_protocol"
    assert status["capacity"] == 10

def test_epaxos_protocol_operations():
    obj = EpaxosProtocol("test_epaxos_protocol_ops", capacity=5)
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
