"""Unit test suite for Oblivious RAM (ORAM) Access Pattern (crypto)."""
from crypto.oram_simulator import OramSimulator

def test_oram_simulator_lifecycle():
    obj = OramSimulator("test_oram_simulator", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_oram_simulator"
    assert status["capacity"] == 10

def test_oram_simulator_operations():
    obj = OramSimulator("test_oram_simulator_ops", capacity=5)
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
