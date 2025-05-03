"""Unit test suite for Intermediate Representation (IR) Codec (compilers)."""
from compilers.ir_codec import IrCodec

def test_ir_codec_lifecycle():
    obj = IrCodec("test_ir_codec", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_ir_codec"
    assert status["capacity"] == 10

def test_ir_codec_operations():
    obj = IrCodec("test_ir_codec_ops", capacity=5)
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
