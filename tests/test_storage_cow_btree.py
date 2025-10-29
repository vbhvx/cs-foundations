"""Unit test suite for Copy-On-Write B-Tree Root Pointers (storage)."""
from storage.cow_btree import CowBtree

def test_cow_btree_lifecycle():
    obj = CowBtree("test_cow_btree", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_cow_btree"
    assert status["capacity"] == 10

def test_cow_btree_operations():
    obj = CowBtree("test_cow_btree_ops", capacity=5)
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
