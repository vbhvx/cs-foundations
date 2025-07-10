"""Unit test suite for QPACK HTTP/3 Header Compression (networking)."""
from networking.qpack_codec import QpackCodec

def test_qpack_codec_lifecycle():
    obj = QpackCodec("test_qpack_codec", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_qpack_codec"
    assert status["capacity"] == 10

def test_qpack_codec_operations():
    obj = QpackCodec("test_qpack_codec_ops", capacity=5)
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
