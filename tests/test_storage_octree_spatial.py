"""Unit test suite for Octree 3D Voxel Spatial Decomposition (storage)."""
from storage.octree_spatial import OctreeSpatial

def test_octree_spatial_lifecycle():
    obj = OctreeSpatial("test_octree_spatial", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_octree_spatial"
    assert status["capacity"] == 10

def test_octree_spatial_operations():
    obj = OctreeSpatial("test_octree_spatial_ops", capacity=5)
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
