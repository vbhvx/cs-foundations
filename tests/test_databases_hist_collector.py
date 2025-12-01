"""Unit test suite for Statistics Histogram Collector (databases)."""
from databases.hist_collector import HistCollector

def test_hist_collector_lifecycle():
    obj = HistCollector("test_hist_collector", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_hist_collector"
    assert status["capacity"] == 10

def test_hist_collector_operations():
    obj = HistCollector("test_hist_collector_ops", capacity=5)
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
