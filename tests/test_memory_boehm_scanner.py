"""Unit test suite for Boehm Conservative Stack Scanner (memory)."""
from memory.boehm_scanner import BoehmScanner

def test_boehm_scanner_lifecycle():
    obj = BoehmScanner("test_boehm_scanner", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_boehm_scanner"
    assert status["capacity"] == 10

def test_boehm_scanner_operations():
    obj = BoehmScanner("test_boehm_scanner_ops", capacity=5)
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
