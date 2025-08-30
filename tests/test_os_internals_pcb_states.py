"""Unit test suite for Process Control Block (PCB) State Machine (os_internals)."""
from os_internals.pcb_states import PcbStates

def test_pcb_states_lifecycle():
    obj = PcbStates("test_pcb_states", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_pcb_states"
    assert status["capacity"] == 10

def test_pcb_states_operations():
    obj = PcbStates("test_pcb_states_ops", capacity=5)
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
