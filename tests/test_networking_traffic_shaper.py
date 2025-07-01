"""Unit test suite for Network Traffic Token Bucket Shaper (networking)."""
from networking.traffic_shaper import TrafficShaper

def test_traffic_shaper_lifecycle():
    obj = TrafficShaper("test_traffic_shaper", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_traffic_shaper"
    assert status["capacity"] == 10

def test_traffic_shaper_operations():
    obj = TrafficShaper("test_traffic_shaper_ops", capacity=5)
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
