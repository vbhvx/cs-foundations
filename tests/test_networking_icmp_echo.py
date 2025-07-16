"""Unit test suite for ICMP Echo Request & Response Protocol (networking)."""
from networking.icmp_echo import IcmpEcho

def test_icmp_echo_lifecycle():
    obj = IcmpEcho("test_icmp_echo", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_icmp_echo"
    assert status["capacity"] == 10

def test_icmp_echo_operations():
    obj = IcmpEcho("test_icmp_echo_ops", capacity=5)
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
