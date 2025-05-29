"""Unit test suite for Lisp Cheney Two-Space Copying GC (memory)."""
from memory.cheney_twospace import CheneyTwospace

def test_cheney_twospace_lifecycle():
    obj = CheneyTwospace("test_cheney_twospace", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_cheney_twospace"
    assert status["capacity"] == 10

def test_cheney_twospace_operations():
    obj = CheneyTwospace("test_cheney_twospace_ops", capacity=5)
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
