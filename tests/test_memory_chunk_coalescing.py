"""Unit test suite for Memory Pool Free List Chunk Coalescing (memory)."""
from memory.chunk_coalescing import ChunkCoalescing

def test_chunk_coalescing_lifecycle():
    obj = ChunkCoalescing("test_chunk_coalescing", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_chunk_coalescing"
    assert status["capacity"] == 10

def test_chunk_coalescing_operations():
    obj = ChunkCoalescing("test_chunk_coalescing_ops", capacity=5)
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
