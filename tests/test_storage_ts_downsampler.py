"""Unit test suite for Time-Series Bucket Downsampling Rollup (storage)."""
from storage.ts_downsampler import TsDownsampler

def test_ts_downsampler_lifecycle():
    obj = TsDownsampler("test_ts_downsampler", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_ts_downsampler"
    assert status["capacity"] == 10

def test_ts_downsampler_operations():
    obj = TsDownsampler("test_ts_downsampler_ops", capacity=5)
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
