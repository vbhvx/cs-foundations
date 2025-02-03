"""Unit test suite for Volcano Iterator Execution Engine (databases)."""
from databases.volcano_iter import VolcanoIter

def test_volcano_iter_lifecycle():
    obj = VolcanoIter("test_volcano_iter", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_volcano_iter"
    assert status["capacity"] == 10

def test_volcano_iter_operations():
    obj = VolcanoIter("test_volcano_iter_ops", capacity=5)
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
