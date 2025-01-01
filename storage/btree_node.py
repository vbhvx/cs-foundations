"""B-Tree node representation for on-disk/in-memory indices."""

class BTreeNode:
    def __init__(self, is_leaf: bool = True):
        self.is_leaf = is_leaf
        self.keys = []
        self.values = []
        self.children = []
