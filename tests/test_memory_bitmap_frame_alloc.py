"""Unit test suite for Bitmapped Free Frame Block Allocator (memory)."""
from memory.bitmap_frame_alloc import BitmapFrameAlloc

def test_bitmap_frame_alloc_lifecycle():
    obj = BitmapFrameAlloc("test_bitmap_frame_alloc", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_bitmap_frame_alloc"
    assert status["capacity"] == 10

def test_bitmap_frame_alloc_operations():
    obj = BitmapFrameAlloc("test_bitmap_frame_alloc_ops", capacity=5)
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
