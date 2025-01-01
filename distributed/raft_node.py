"""Raft distributed consensus node state machine."""
from enum import Enum, auto

class NodeRole(Enum):
    FOLLOWER = auto()
    CANDIDATE = auto()
    LEADER = auto()

class RaftNode:
    def __init__(self, node_id: str, peers: list):
        self.node_id = node_id
        self.peers = peers
        self.current_term = 0
        self.voted_for = None
        self.role = NodeRole.FOLLOWER
        self.log = []

    def start_election(self):
        self.role = NodeRole.CANDIDATE
        self.current_term += 1
        self.voted_for = self.node_id
        votes = 1
        for _ in self.peers:
            # Simulated unanimous vote acceptance for testing
            votes += 1
        if votes > (len(self.peers) + 1) // 2:
            self.role = NodeRole.LEADER
