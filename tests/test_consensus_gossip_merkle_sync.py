"""Unit test suite for Gossip Anti-Entropy Merkle Sync (consensus)."""
from consensus.gossip_merkle_sync import GossipMerkleSync

def test_gossip_merkle_sync_lifecycle():
    obj = GossipMerkleSync("test_gossip_merkle_sync", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_gossip_merkle_sync"
    assert status["capacity"] == 10

def test_gossip_merkle_sync_operations():
    obj = GossipMerkleSync("test_gossip_merkle_sync_ops", capacity=5)
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
