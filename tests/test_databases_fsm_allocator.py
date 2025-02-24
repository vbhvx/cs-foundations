"""Unit test suite for Free Space Map (FSM) Allocator (databases)."""
from databases.fsm_allocator import FsmAllocator

def test_fsm_allocator_lifecycle():
    obj = FsmAllocator("test_fsm_allocator", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_fsm_allocator"
    assert status["capacity"] == 10

def test_fsm_allocator_operations():
    obj = FsmAllocator("test_fsm_allocator_ops", capacity=5)
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
