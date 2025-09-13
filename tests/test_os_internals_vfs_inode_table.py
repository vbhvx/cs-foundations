"""Unit test suite for Unix VFS (Virtual File System) Inode Table (os_internals)."""
from os_internals.vfs_inode_table import VfsInodeTable

def test_vfs_inode_table_lifecycle():
    obj = VfsInodeTable("test_vfs_inode_table", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_vfs_inode_table"
    assert status["capacity"] == 10

def test_vfs_inode_table_operations():
    obj = VfsInodeTable("test_vfs_inode_table_ops", capacity=5)
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
