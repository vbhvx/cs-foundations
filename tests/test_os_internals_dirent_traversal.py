"""Unit test suite for Directory Entry (dirent) Linear Traversal (os_internals)."""
from os_internals.dirent_traversal import DirentTraversal

def test_dirent_traversal_lifecycle():
    obj = DirentTraversal("test_dirent_traversal", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_dirent_traversal"
    assert status["capacity"] == 10

def test_dirent_traversal_operations():
    obj = DirentTraversal("test_dirent_traversal_ops", capacity=5)
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
