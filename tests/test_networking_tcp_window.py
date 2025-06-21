"""Unit test suite for TCP Sliding Window Flow Control (networking)."""
from networking.tcp_window import TcpWindow

def test_tcp_window_lifecycle():
    obj = TcpWindow("test_tcp_window", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_tcp_window"
    assert status["capacity"] == 10

def test_tcp_window_operations():
    obj = TcpWindow("test_tcp_window_ops", capacity=5)
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
