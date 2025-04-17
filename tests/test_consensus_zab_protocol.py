"""Unit test suite for Zab (ZooKeeper Atomic Broadcast) (consensus)."""
from consensus.zab_protocol import ZabProtocol

def test_zab_protocol_lifecycle():
    obj = ZabProtocol("test_zab_protocol", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_zab_protocol"
    assert status["capacity"] == 10

def test_zab_protocol_operations():
    obj = ZabProtocol("test_zab_protocol_ops", capacity=5)
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
