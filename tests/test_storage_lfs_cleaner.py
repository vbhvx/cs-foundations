"""Unit test suite for Log-Structured Object Store Garbage Collector (storage)."""
from storage.lfs_cleaner import LfsCleaner

def test_lfs_cleaner_lifecycle():
    obj = LfsCleaner("test_lfs_cleaner", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_lfs_cleaner"
    assert status["capacity"] == 10

def test_lfs_cleaner_operations():
    obj = LfsCleaner("test_lfs_cleaner_ops", capacity=5)
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
