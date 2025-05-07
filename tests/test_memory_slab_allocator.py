"""Unit test suite for Slab Memory Allocator (memory)."""
from memory.slab_allocator import SlabAllocator

def test_slab_allocator_lifecycle():
    obj = SlabAllocator("test_slab_allocator", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_slab_allocator"
    assert status["capacity"] == 10

def test_slab_allocator_operations():
    obj = SlabAllocator("test_slab_allocator_ops", capacity=5)
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
