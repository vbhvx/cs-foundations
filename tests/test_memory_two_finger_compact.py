"""Unit test suite for Two-Finger Compaction Algorithm (memory)."""
from memory.two_finger_compact import TwoFingerCompact

def test_two_finger_compact_lifecycle():
    obj = TwoFingerCompact("test_two_finger_compact", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_two_finger_compact"
    assert status["capacity"] == 10

def test_two_finger_compact_operations():
    obj = TwoFingerCompact("test_two_finger_compact_ops", capacity=5)
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
