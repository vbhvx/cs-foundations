"""Unit test suite for Memory Mapped File Paging Region (memory)."""
from memory.mmap_region import MmapRegion

def test_mmap_region_lifecycle():
    obj = MmapRegion("test_mmap_region", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_mmap_region"
    assert status["capacity"] == 10

def test_mmap_region_operations():
    obj = MmapRegion("test_mmap_region_ops", capacity=5)
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
