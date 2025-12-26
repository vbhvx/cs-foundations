"""Unit test suite for Atomic Multicast Group Membership State (distributed)."""
from distributed.group_membership import GroupMembership

def test_group_membership_lifecycle():
    obj = GroupMembership("test_group_membership", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_group_membership"
    assert status["capacity"] == 10

def test_group_membership_operations():
    obj = GroupMembership("test_group_membership_ops", capacity=5)
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
