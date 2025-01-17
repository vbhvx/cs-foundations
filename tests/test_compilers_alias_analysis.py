"""Unit test suite for Alias Analysis & Pointer Disambiguation (compilers)."""
from compilers.alias_analysis import AliasAnalysis

def test_alias_analysis_lifecycle():
    obj = AliasAnalysis("test_alias_analysis", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_alias_analysis"
    assert status["capacity"] == 10

def test_alias_analysis_operations():
    obj = AliasAnalysis("test_alias_analysis_ops", capacity=5)
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
