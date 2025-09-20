"""Unit test suite for Seccomp BPF System Call Filter (os_internals)."""
from os_internals.seccomp_filter import SeccompFilter

def test_seccomp_filter_lifecycle():
    obj = SeccompFilter("test_seccomp_filter", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_seccomp_filter"
    assert status["capacity"] == 10

def test_seccomp_filter_operations():
    obj = SeccompFilter("test_seccomp_filter_ops", capacity=5)
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
