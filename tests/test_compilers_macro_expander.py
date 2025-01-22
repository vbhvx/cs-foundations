"""Unit test suite for Macro Expander & Preprocessor (compilers)."""
from compilers.macro_expander import MacroExpander

def test_macro_expander_lifecycle():
    obj = MacroExpander("test_macro_expander", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_macro_expander"
    assert status["capacity"] == 10

def test_macro_expander_operations():
    obj = MacroExpander("test_macro_expander_ops", capacity=5)
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
