"""Unit test suite for H3 Hexagonal Hierarchical Spatial Index (storage)."""
from storage.h3_hex_index import H3HexIndex

def test_h3_hex_index_lifecycle():
    obj = H3HexIndex("test_h3_hex_index", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_h3_hex_index"
    assert status["capacity"] == 10

def test_h3_hex_index_operations():
    obj = H3HexIndex("test_h3_hex_index_ops", capacity=5)
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
