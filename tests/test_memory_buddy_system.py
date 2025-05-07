"""Unit test suite for Buddy Memory System (memory)."""
from memory.buddy_system import BuddySystem

def test_buddy_system_lifecycle():
    obj = BuddySystem("test_buddy_system", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_buddy_system"
    assert status["capacity"] == 10

def test_buddy_system_operations():
    obj = BuddySystem("test_buddy_system_ops", capacity=5)
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
