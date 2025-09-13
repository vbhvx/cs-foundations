"""Unit test suite for Ext2 Superblock & Block Group Descriptor (os_internals)."""
from os_internals.ext2_superblock import Ext2Superblock

def test_ext2_superblock_lifecycle():
    obj = Ext2Superblock("test_ext2_superblock", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_ext2_superblock"
    assert status["capacity"] == 10

def test_ext2_superblock_operations():
    obj = Ext2Superblock("test_ext2_superblock_ops", capacity=5)
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
