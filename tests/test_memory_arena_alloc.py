"""Unit test suite for Arena Bump Allocator (memory)."""
from memory.arena_alloc import ArenaAlloc

def test_arena_alloc_lifecycle():
    obj = ArenaAlloc("test_arena_alloc", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_arena_alloc"
    assert status["capacity"] == 10

def test_arena_alloc_operations():
    obj = ArenaAlloc("test_arena_alloc_ops", capacity=5)
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
