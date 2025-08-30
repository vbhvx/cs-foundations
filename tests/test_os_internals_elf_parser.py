"""Unit test suite for ELF 64-Bit Binary Header Parser (os_internals)."""
from os_internals.elf_parser import ElfParser

def test_elf_parser_lifecycle():
    obj = ElfParser("test_elf_parser", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_elf_parser"
    assert status["capacity"] == 10

def test_elf_parser_operations():
    obj = ElfParser("test_elf_parser_ops", capacity=5)
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
