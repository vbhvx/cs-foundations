"""Unit test suite for QUIC Variable-Length Integer Codec (networking)."""
from networking.quic_varint import QuicVarint

def test_quic_varint_lifecycle():
    obj = QuicVarint("test_quic_varint", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_quic_varint"
    assert status["capacity"] == 10

def test_quic_varint_operations():
    obj = QuicVarint("test_quic_varint_ops", capacity=5)
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
