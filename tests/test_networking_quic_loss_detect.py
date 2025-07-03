"""Unit test suite for QUIC Loss Detection & Recovery (networking)."""
from networking.quic_loss_detect import QuicLossDetect

def test_quic_loss_detect_lifecycle():
    obj = QuicLossDetect("test_quic_loss_detect", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_quic_loss_detect"
    assert status["capacity"] == 10

def test_quic_loss_detect_operations():
    obj = QuicLossDetect("test_quic_loss_detect_ops", capacity=5)
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
