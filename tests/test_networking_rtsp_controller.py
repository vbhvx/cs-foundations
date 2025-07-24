"""Unit test suite for RTSP Streaming Session State Controller (networking)."""
from networking.rtsp_controller import RtspController

def test_rtsp_controller_lifecycle():
    obj = RtspController("test_rtsp_controller", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_rtsp_controller"
    assert status["capacity"] == 10

def test_rtsp_controller_operations():
    obj = RtspController("test_rtsp_controller_ops", capacity=5)
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
