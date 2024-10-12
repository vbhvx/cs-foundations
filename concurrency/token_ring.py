"""Token ring distributed mutual exclusion model."""

class TokenRingNode:
    def __init__(self, node_id: int, num_nodes: int):
        self.node_id = node_id
        self.next_node = (node_id + 1) % num_nodes
        self.has_token = (node_id == 0)
        self.in_critical_section = False

    def pass_token(self, ring):
        if self.has_token and not self.in_critical_section:
            self.has_token = False
            ring[self.next_node].has_token = True
