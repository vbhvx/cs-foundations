"""Unit test suite for Zero-Fill On-Demand Virtual Page (memory)."""
from memory.zfd_virtual_page import ZfdVirtualPage

def test_zfd_virtual_page_lifecycle():
    obj = ZfdVirtualPage("test_zfd_virtual_page", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_zfd_virtual_page"
    assert status["capacity"] == 10

def test_zfd_virtual_page_operations():
    obj = ZfdVirtualPage("test_zfd_virtual_page_ops", capacity=5)
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
