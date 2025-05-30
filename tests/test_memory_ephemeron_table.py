"""Unit test suite for Weak Reference Ephemeron Table (memory)."""
from memory.ephemeron_table import EphemeronTable

def test_ephemeron_table_lifecycle():
    obj = EphemeronTable("test_ephemeron_table", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_ephemeron_table"
    assert status["capacity"] == 10

def test_ephemeron_table_operations():
    obj = EphemeronTable("test_ephemeron_table_ops", capacity=5)
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
