"""Unit test suite for Function Inlining Heuristic (compilers)."""
from compilers.inlining_heuristic import InliningHeuristic

def test_inlining_heuristic_lifecycle():
    obj = InliningHeuristic("test_inlining_heuristic", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_inlining_heuristic"
    assert status["capacity"] == 10

def test_inlining_heuristic_operations():
    obj = InliningHeuristic("test_inlining_heuristic_ops", capacity=5)
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
