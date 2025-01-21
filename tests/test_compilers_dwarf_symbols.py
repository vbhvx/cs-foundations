"""Unit test suite for DWARF Debug Symbol Generator (compilers)."""
from compilers.dwarf_symbols import DwarfSymbols

def test_dwarf_symbols_lifecycle():
    obj = DwarfSymbols("test_dwarf_symbols", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_dwarf_symbols"
    assert status["capacity"] == 10

def test_dwarf_symbols_operations():
    obj = DwarfSymbols("test_dwarf_symbols_ops", capacity=5)
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
