"""Unit test suite for Virtual Memory Two-Level Page Table (os_internals)."""
from os_internals.page_table_two_level import PageTableTwoLevel

def test_page_table_two_level_lifecycle():
    obj = PageTableTwoLevel("test_page_table_two_level", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_page_table_two_level"
    assert status["capacity"] == 10

def test_page_table_two_level_operations():
    obj = PageTableTwoLevel("test_page_table_two_level_ops", capacity=5)
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
