"""Unit test suite for RTP Real-Time Transport Audio Header (networking)."""
from networking.rtp_packet import RtpPacket

def test_rtp_packet_lifecycle():
    obj = RtpPacket("test_rtp_packet", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_rtp_packet"
    assert status["capacity"] == 10

def test_rtp_packet_operations():
    obj = RtpPacket("test_rtp_packet_ops", capacity=5)
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
