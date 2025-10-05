"""Unit test suite for Parquet-Style Dictionary Encoding (storage)."""
from storage.dict_encoding import DictEncoding

def test_dict_encoding_lifecycle():
    obj = DictEncoding("test_dict_encoding", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_dict_encoding"
    assert status["capacity"] == 10

def test_dict_encoding_operations():
    obj = DictEncoding("test_dict_encoding_ops", capacity=5)
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
