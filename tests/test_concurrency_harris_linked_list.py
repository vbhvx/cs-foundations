"""Unit test suite for Harris Lock-Free Linked List with CAS (concurrency)."""
from concurrency.harris_linked_list import HarrisLinkedList

def test_harris_linked_list_lifecycle():
    obj = HarrisLinkedList("test_harris_linked_list", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_harris_linked_list"
    assert status["capacity"] == 10

def test_harris_linked_list_operations():
    obj = HarrisLinkedList("test_harris_linked_list_ops", capacity=5)
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
