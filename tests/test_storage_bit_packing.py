"""Unit test suite for Bit-Packed Integer Compression (storage)."""
from storage.bit_packing import BitPacking

def test_bit_packing_lifecycle():
    obj = BitPacking("test_bit_packing", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_bit_packing"
    assert status["capacity"] == 10

def test_bit_packing_operations():
    obj = BitPacking("test_bit_packing_ops", capacity=5)
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
