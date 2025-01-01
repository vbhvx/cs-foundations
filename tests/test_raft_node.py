from distributed.raft_node import RaftNode, NodeRole

def test_raft_election():
    node = RaftNode("N1", ["N2", "N3"])
    assert node.role == NodeRole.FOLLOWER
    node.start_election()
    assert node.role == NodeRole.LEADER
    assert node.current_term == 1
