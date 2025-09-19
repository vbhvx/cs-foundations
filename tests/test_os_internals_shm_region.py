"""Unit test suite for Shared Memory POSIX shm Region (os_internals)."""
from os_internals.shm_region import ShmRegion

def test_shm_region_lifecycle():
    obj = ShmRegion("test_shm_region", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_shm_region"
    assert status["capacity"] == 10

def test_shm_region_operations():
    obj = ShmRegion("test_shm_region_ops", capacity=5)
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
