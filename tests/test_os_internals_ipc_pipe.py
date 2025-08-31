"""Unit test suite for Unix IPC Pipe Ring Buffer (os_internals)."""
from os_internals.ipc_pipe import IpcPipe

def test_ipc_pipe_lifecycle():
    obj = IpcPipe("test_ipc_pipe", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_ipc_pipe"
    assert status["capacity"] == 10

def test_ipc_pipe_operations():
    obj = IpcPipe("test_ipc_pipe_ops", capacity=5)
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
