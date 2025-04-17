"""Unit test suite for Gossip Epidemic Dissemination (consensus)."""
from consensus.gossip_dissem import GossipDissem

def test_gossip_dissem_lifecycle():
    obj = GossipDissem("test_gossip_dissem", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_gossip_dissem"
    assert status["capacity"] == 10

def test_gossip_dissem_operations():
    obj = GossipDissem("test_gossip_dissem_ops", capacity=5)
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
