"""Unit test suite for Kernel Memory Buddy Page Allocator (os_internals)."""
from os_internals.buddy_page_alloc import BuddyPageAlloc

def test_buddy_page_alloc_lifecycle():
    obj = BuddyPageAlloc("test_buddy_page_alloc", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_buddy_page_alloc"
    assert status["capacity"] == 10

def test_buddy_page_alloc_operations():
    obj = BuddyPageAlloc("test_buddy_page_alloc_ops", capacity=5)
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
