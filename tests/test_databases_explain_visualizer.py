"""Unit test suite for Query Plan Explain Visualizer (databases)."""
from databases.explain_visualizer import ExplainVisualizer

def test_explain_visualizer_lifecycle():
    obj = ExplainVisualizer("test_explain_visualizer", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_explain_visualizer"
    assert status["capacity"] == 10

def test_explain_visualizer_operations():
    obj = ExplainVisualizer("test_explain_visualizer_ops", capacity=5)
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
