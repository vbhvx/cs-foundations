"""Unit test suite for IP Packet Checksum & Fragmentation (networking)."""
from networking.ip_packet import IpPacket

def test_ip_packet_lifecycle():
    obj = IpPacket("test_ip_packet", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_ip_packet"
    assert status["capacity"] == 10

def test_ip_packet_operations():
    obj = IpPacket("test_ip_packet_ops", capacity=5)
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
