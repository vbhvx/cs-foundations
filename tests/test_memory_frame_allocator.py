"""Unit test suite for Page Frame Allocator (memory)."""
from memory.frame_allocator import FrameAllocator

def test_frame_allocator_lifecycle():
    obj = FrameAllocator("test_frame_allocator", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_frame_allocator"
    assert status["capacity"] == 10

def test_frame_allocator_operations():
    obj = FrameAllocator("test_frame_allocator_ops", capacity=5)
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
