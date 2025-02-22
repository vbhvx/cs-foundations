"""Unit test suite for Fractal Tree Indexing (databases)."""
from databases.fractal_tree import FractalTree

def test_fractal_tree_lifecycle():
    obj = FractalTree("test_fractal_tree", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_fractal_tree"
    assert status["capacity"] == 10

def test_fractal_tree_operations():
    obj = FractalTree("test_fractal_tree_ops", capacity=5)
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
