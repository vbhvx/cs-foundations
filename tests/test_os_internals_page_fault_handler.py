"""Unit test suite for Demand Paging Page Fault Handler (os_internals)."""
from os_internals.page_fault_handler import PageFaultHandler

def test_page_fault_handler_lifecycle():
    obj = PageFaultHandler("test_page_fault_handler", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_page_fault_handler"
    assert status["capacity"] == 10

def test_page_fault_handler_operations():
    obj = PageFaultHandler("test_page_fault_handler_ops", capacity=5)
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
