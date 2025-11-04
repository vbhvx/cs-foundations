"""Unit test suite for Fenwick Tree Binary Indexed Cumulative Count (storage)."""
from storage.fenwick_storage import FenwickStorage

def test_fenwick_storage_lifecycle():
    obj = FenwickStorage("test_fenwick_storage", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_fenwick_storage"
    assert status["capacity"] == 10

def test_fenwick_storage_operations():
    obj = FenwickStorage("test_fenwick_storage_ops", capacity=5)
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
