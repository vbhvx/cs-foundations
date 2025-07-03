"""Unit test suite for Delayed ACK Timer State Machine (networking)."""
from networking.delayed_ack import DelayedAck

def test_delayed_ack_lifecycle():
    obj = DelayedAck("test_delayed_ack", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_delayed_ack"
    assert status["capacity"] == 10

def test_delayed_ack_operations():
    obj = DelayedAck("test_delayed_ack_ops", capacity=5)
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
