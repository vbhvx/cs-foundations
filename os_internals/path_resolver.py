"""Hierarchical filesystem directory path traversal."""
from typing import Dict
from os_internals.inode import Inode

class SimpleFS:
    def __init__(self):
        self.root_inode = Inode(0, is_dir=True)
        self.inodes: Dict[int, Inode] = {0: self.root_inode}
        self.directories: Dict[int, Dict[str, int]] = {0: {}}
        self._next_inode = 1

    def mkdir(self, parent_id: int, name: str) -> int:
        ino_id = self._next_inode
        self._next_inode += 1
        self.inodes[ino_id] = Inode(ino_id, is_dir=True)
        self.directories[ino_id] = {}
        self.directories[parent_id][name] = ino_id
        return ino_id

    def resolve(self, path: str) -> int:
        parts = [p for p in path.split("/") if p]
        cur = 0
        for p in parts:
            if p not in self.directories[cur]:
                raise FileNotFoundError(f"Path not found: {path}")
            cur = self.directories[cur][p]
        return cur
