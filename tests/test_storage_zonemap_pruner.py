"""Unit test suite for Zone Map Min-Max Pruning Index (storage)."""
from storage.zonemap_pruner import ZonemapPruner

def test_zonemap_pruner_lifecycle():
    obj = ZonemapPruner("test_zonemap_pruner", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_zonemap_pruner"
    assert status["capacity"] == 10

def test_zonemap_pruner_operations():
    obj = ZonemapPruner("test_zonemap_pruner_ops", capacity=5)
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
