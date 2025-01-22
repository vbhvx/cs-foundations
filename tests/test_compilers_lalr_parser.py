"""Unit test suite for LALR Parser State Machine (compilers)."""
from compilers.lalr_parser import LalrParser

def test_lalr_parser_lifecycle():
    obj = LalrParser("test_lalr_parser", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_lalr_parser"
    assert status["capacity"] == 10

def test_lalr_parser_operations():
    obj = LalrParser("test_lalr_parser_ops", capacity=5)
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
