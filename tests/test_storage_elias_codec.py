"""Unit test suite for Elias-Gamma & Elias-Delta Integer Codec (storage)."""
from storage.elias_codec import EliasCodec

def test_elias_codec_lifecycle():
    obj = EliasCodec("test_elias_codec", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_elias_codec"
    assert status["capacity"] == 10

def test_elias_codec_operations():
    obj = EliasCodec("test_elias_codec_ops", capacity=5)
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
