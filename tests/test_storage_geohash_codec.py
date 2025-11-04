"""Unit test suite for Geohash Spatial Location Encoder (storage)."""
from storage.geohash_codec import GeohashCodec

def test_geohash_codec_lifecycle():
    obj = GeohashCodec("test_geohash_codec", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_geohash_codec"
    assert status["capacity"] == 10

def test_geohash_codec_operations():
    obj = GeohashCodec("test_geohash_codec_ops", capacity=5)
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
