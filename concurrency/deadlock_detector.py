"""Cycle detection in resource allocation graphs using DFS."""
from typing import Dict, Set, List

class WaitForGraph:
    def __init__(self):
        self._edges: Dict[str, Set[str]] = {}

    def add_dependency(self, waiting_txn: str, holding_txn: str):
        if waiting_txn not in self._edges:
            self._edges[waiting_txn] = set()
        self._edges[waiting_txn].add(holding_txn)

    def remove_dependency(self, waiting_txn: str, holding_txn: str):
        if waiting_txn in self._edges:
            self._edges[waiting_txn].discard(holding_txn)

    def detect_deadlock(self) -> List[str]:
        visited = set()
        rec_stack = set()
        cycle = []

        def dfs(node: str, path: List[str]) -> bool:
            visited.add(node)
            rec_stack.add(node)
            for neighbor in self._edges.get(node, []):
                if neighbor not in visited:
                    if dfs(neighbor, path + [neighbor]):
                        return True
                elif neighbor in rec_stack:
                    cycle.extend(path + [neighbor])
                    return True
            rec_stack.remove(node)
            return False

        for node in list(self._edges.keys()):
            if node not in visited:
                if dfs(node, [node]):
                    return cycle
        return []
