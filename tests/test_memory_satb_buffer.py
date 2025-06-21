"""Unit test suite for Concurrent Marking SATB Buffer (memory)."""
from memory.satb_buffer import SatbBuffer

def test_satb_buffer_lifecycle():
    obj = SatbBuffer("test_satb_buffer", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_satb_buffer"
    assert status["capacity"] == 10

def test_satb_buffer_operations():
    obj = SatbBuffer("test_satb_buffer_ops", capacity=5)
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
