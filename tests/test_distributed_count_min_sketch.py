"""Unit test suite for Count-Min Sketch Frequency Estimator (distributed)."""
from distributed.count_min_sketch import CountMinSketch

def test_count_min_sketch_lifecycle():
    obj = CountMinSketch("test_count_min_sketch", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_count_min_sketch"
    assert status["capacity"] == 10

def test_count_min_sketch_operations():
    obj = CountMinSketch("test_count_min_sketch_ops", capacity=5)
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
