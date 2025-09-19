"""Unit test suite for Kernel Timer Wheel Millisecond Tick (os_internals)."""
from os_internals.timer_wheel import TimerWheel

def test_timer_wheel_lifecycle():
    obj = TimerWheel("test_timer_wheel", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_timer_wheel"
    assert status["capacity"] == 10

def test_timer_wheel_operations():
    obj = TimerWheel("test_timer_wheel_ops", capacity=5)
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
