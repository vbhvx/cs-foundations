"""Unit test suite for Cgroups CPU Quota Bandwidth Enforcer (os_internals)."""
from os_internals.cgroup_cpu_quota import CgroupCpuQuota

def test_cgroup_cpu_quota_lifecycle():
    obj = CgroupCpuQuota("test_cgroup_cpu_quota", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_cgroup_cpu_quota"
    assert status["capacity"] == 10

def test_cgroup_cpu_quota_operations():
    obj = CgroupCpuQuota("test_cgroup_cpu_quota_ops", capacity=5)
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
