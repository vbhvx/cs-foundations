"""Unit test suite for TCP Cubic Congestion Avoidance (networking)."""
from networking.tcp_cubic import TcpCubic

def test_tcp_cubic_lifecycle():
    obj = TcpCubic("test_tcp_cubic", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_tcp_cubic"
    assert status["capacity"] == 10

def test_tcp_cubic_operations():
    obj = TcpCubic("test_tcp_cubic_ops", capacity=5)
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
