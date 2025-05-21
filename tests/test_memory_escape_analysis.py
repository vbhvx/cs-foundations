"""Unit test suite for Escape Analysis Optimization (memory)."""
from memory.escape_analysis import EscapeAnalysis

def test_escape_analysis_lifecycle():
    obj = EscapeAnalysis("test_escape_analysis", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_escape_analysis"
    assert status["capacity"] == 10

def test_escape_analysis_operations():
    obj = EscapeAnalysis("test_escape_analysis_ops", capacity=5)
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
