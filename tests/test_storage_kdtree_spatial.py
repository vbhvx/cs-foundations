"""Unit test suite for KD-Tree Multi-Dimensional Point Index (storage)."""
from storage.kdtree_spatial import KdtreeSpatial

def test_kdtree_spatial_lifecycle():
    obj = KdtreeSpatial("test_kdtree_spatial", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_kdtree_spatial"
    assert status["capacity"] == 10

def test_kdtree_spatial_operations():
    obj = KdtreeSpatial("test_kdtree_spatial_ops", capacity=5)
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
