"""Unit test suite for Epoll Event Multiplexer Simulation (os_internals)."""
from os_internals.epoll_multiplexer import EpollMultiplexer

def test_epoll_multiplexer_lifecycle():
    obj = EpollMultiplexer("test_epoll_multiplexer", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_epoll_multiplexer"
    assert status["capacity"] == 10

def test_epoll_multiplexer_operations():
    obj = EpollMultiplexer("test_epoll_multiplexer_ops", capacity=5)
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
