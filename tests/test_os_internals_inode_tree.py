"""Unit test suite for Inode File System Directory Tree (os_internals)."""
from os_internals.inode_tree import InodeTree

def test_inode_tree_lifecycle():
    obj = InodeTree("test_inode_tree", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_inode_tree"
    assert status["capacity"] == 10

def test_inode_tree_operations():
    obj = InodeTree("test_inode_tree_ops", capacity=5)
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
