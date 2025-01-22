"""Unit test suite for Abstract Syntax Tree Printer (compilers)."""
from compilers.ast_printer import AstPrinter

def test_ast_printer_lifecycle():
    obj = AstPrinter("test_ast_printer", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_ast_printer"
    assert status["capacity"] == 10

def test_ast_printer_operations():
    obj = AstPrinter("test_ast_printer_ops", capacity=5)
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
