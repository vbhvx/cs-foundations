"""Unit test suite for Type Checker & Inference (compilers)."""
from compilers.type_checker import TypeChecker

def test_type_checker_lifecycle():
    obj = TypeChecker("test_type_checker", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_type_checker"
    assert status["capacity"] == 10

def test_type_checker_operations():
    obj = TypeChecker("test_type_checker_ops", capacity=5)
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
