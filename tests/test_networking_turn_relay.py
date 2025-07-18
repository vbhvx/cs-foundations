"""Unit test suite for TURN Relay Allocation Request Protocol (networking)."""
from networking.turn_relay import TurnRelay

def test_turn_relay_lifecycle():
    obj = TurnRelay("test_turn_relay", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_turn_relay"
    assert status["capacity"] == 10

def test_turn_relay_operations():
    obj = TurnRelay("test_turn_relay_ops", capacity=5)
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
