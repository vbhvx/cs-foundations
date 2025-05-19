"""Unit test suite for Copy-on-Write (COW) Memory Page (memory)."""
from memory.cow_page import CowPage

def test_cow_page_lifecycle():
    obj = CowPage("test_cow_page", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_cow_page"
    assert status["capacity"] == 10

def test_cow_page_operations():
    obj = CowPage("test_cow_page_ops", capacity=5)
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
