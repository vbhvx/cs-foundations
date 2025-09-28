"""Unit test suite for Spatial R-Tree Index (storage)."""
from storage.rtree_spatial_idx import RtreeSpatialIdx

def test_rtree_spatial_idx_lifecycle():
    obj = RtreeSpatialIdx("test_rtree_spatial_idx", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_rtree_spatial_idx"
    assert status["capacity"] == 10

def test_rtree_spatial_idx_operations():
    obj = RtreeSpatialIdx("test_rtree_spatial_idx_ops", capacity=5)
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
