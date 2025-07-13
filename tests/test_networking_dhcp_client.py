"""Unit test suite for DHCP Client State Machine & Lease Renew (networking)."""
from networking.dhcp_client import DhcpClient

def test_dhcp_client_lifecycle():
    obj = DhcpClient("test_dhcp_client", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_dhcp_client"
    assert status["capacity"] == 10

def test_dhcp_client_operations():
    obj = DhcpClient("test_dhcp_client_ops", capacity=5)
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
