from distributed.consistent_hashing import ConsistentHashRing

def test_consistent_hash():
    ring = ConsistentHashRing(replicas=50)
    ring.add_node("node1")
    ring.add_node("node2")
    n = ring.get_node("user_session_42")
    assert n in ["node1", "node2"]
