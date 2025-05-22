"""Unit test suite for Zero-Cost Exception Handling Table (compilers)."""
from compilers.exception_table import ExceptionTable

def test_exception_table_lifecycle():
    obj = ExceptionTable("test_exception_table", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_exception_table"
    assert status["capacity"] == 10

def test_exception_table_operations():
    obj = ExceptionTable("test_exception_table_ops", capacity=5)
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
