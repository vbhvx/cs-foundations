"""Unit test suite for TCP SYN Cookie Flood Protection (networking)."""
from networking.tcp_syncookie import TcpSyncookie

def test_tcp_syncookie_lifecycle():
    obj = TcpSyncookie("test_tcp_syncookie", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_tcp_syncookie"
    assert status["capacity"] == 10

def test_tcp_syncookie_operations():
    obj = TcpSyncookie("test_tcp_syncookie_ops", capacity=5)
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
