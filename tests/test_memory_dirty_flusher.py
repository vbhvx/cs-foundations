"""Unit test suite for Dirty Page Background Writeback Flusher (memory)."""
from memory.dirty_flusher import DirtyFlusher

def test_dirty_flusher_lifecycle():
    obj = DirtyFlusher("test_dirty_flusher", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_dirty_flusher"
    assert status["capacity"] == 10

def test_dirty_flusher_operations():
    obj = DirtyFlusher("test_dirty_flusher_ops", capacity=5)
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
