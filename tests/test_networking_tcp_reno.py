"""Unit test suite for TCP Congestion Control (Tahoe & Reno) (networking)."""
from networking.tcp_reno import TcpReno

def test_tcp_reno_lifecycle():
    obj = TcpReno("test_tcp_reno", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_tcp_reno"
    assert status["capacity"] == 10

def test_tcp_reno_operations():
    obj = TcpReno("test_tcp_reno_ops", capacity=5)
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
