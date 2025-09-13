"""Unit test suite for File Descriptor Table with O_CLOEXEC Flags (os_internals)."""
from os_internals.fd_table import FdTable

def test_fd_table_lifecycle():
    obj = FdTable("test_fd_table", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_fd_table"
    assert status["capacity"] == 10

def test_fd_table_operations():
    obj = FdTable("test_fd_table_ops", capacity=5)
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
