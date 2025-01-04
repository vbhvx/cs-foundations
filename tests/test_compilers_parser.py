"""Unit test suite for Recursive Descent Parser (compilers)."""
from compilers.parser import Parser

def test_parser_lifecycle():
    obj = Parser("test_parser", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_parser"
    assert status["capacity"] == 10

def test_parser_operations():
    obj = Parser("test_parser_ops", capacity=5)
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
