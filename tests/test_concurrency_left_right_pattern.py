"""Unit test suite for Left-Right Concurrency Pattern (concurrency)."""
from concurrency.left_right_pattern import LeftRightPattern

def test_left_right_pattern_lifecycle():
    obj = LeftRightPattern("test_left_right_pattern", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_left_right_pattern"
    assert status["capacity"] == 10

def test_left_right_pattern_operations():
    obj = LeftRightPattern("test_left_right_pattern_ops", capacity=5)
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
