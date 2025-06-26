"""Unit test suite for HPACK Header Compression (RFC 7541) (networking)."""
from networking.hpack_codec import HpackCodec

def test_hpack_codec_lifecycle():
    obj = HpackCodec("test_hpack_codec", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_hpack_codec"
    assert status["capacity"] == 10

def test_hpack_codec_operations():
    obj = HpackCodec("test_hpack_codec_ops", capacity=5)
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
