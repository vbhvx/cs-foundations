"""Vector Clock tracking causal history in distributed nodes."""
from typing import Dict

class VectorClock:
    def __init__(self, node_id: str):
        self.node_id = node_id
        self.clock: Dict[str, int] = {node_id: 0}

    def tick(self):
        self.clock[self.node_id] = self.clock.get(self.node_id, 0) + 1

    def send(self) -> dict:
        self.tick()
        return dict(self.clock)

    def receive(self, incoming: dict):
        for node, time in incoming.items():
            self.clock[node] = max(self.clock.get(node, 0), time)
        self.tick()

    @staticmethod
    def compare(vc1: dict, vc2: dict) -> str:
        all_keys = set(vc1.keys()) | set(vc2.keys())
        vc1_less = False
        vc2_less = False
        for k in all_keys:
            t1 = vc1.get(k, 0)
            t2 = vc2.get(k, 0)
            if t1 < t2: vc1_less = True
            if t1 > t2: vc2_less = True
        if vc1_less and not vc2_less: return "BEFORE"
        if vc2_less and not vc1_less: return "AFTER"
        if not vc1_less and not vc2_less: return "EQUAL"
        return "CONCURRENT"
