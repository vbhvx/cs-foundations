"""Unit test suite for Escape Analysis Pass (compilers)."""
from compilers.escape_pass import EscapePass

def test_escape_pass_lifecycle():
    obj = EscapePass("test_escape_pass", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_escape_pass"
    assert status["capacity"] == 10

def test_escape_pass_operations():
    obj = EscapePass("test_escape_pass_ops", capacity=5)
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
