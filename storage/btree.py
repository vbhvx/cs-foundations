"""B-Tree order-M self-balancing search tree."""
from storage.btree_node import BTreeNode

class BTree:
    def __init__(self, t: int = 2): # Minimum degree t
        self.root = BTreeNode(is_leaf=True)
        self.t = t

    def search(self, key: str, node: BTreeNode = None):
        if node is None: node = self.root
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            return node.values[i]
        if node.is_leaf:
            return None
        return self.search(key, node.children[i])

    def insert(self, key: str, value: str):
        root = self.root
        if len(root.keys) == (2 * self.t - 1):
            s = BTreeNode(is_leaf=False)
            self.root = s
            s.children.append(root)
            self._split_child(s, 0, root)
            self._insert_non_full(s, key, value)
        else:
            self._insert_non_full(root, key, value)

    def _split_child(self, parent: BTreeNode, i: int, child: BTreeNode):
        t = self.t
        z = BTreeNode(is_leaf=child.is_leaf)
        parent.children.insert(i + 1, z)
        parent.keys.insert(i, child.keys[t - 1])
        parent.values.insert(i, child.values[t - 1])
        z.keys = child.keys[t:(2 * t - 1)]
        z.values = child.values[t:(2 * t - 1)]
        child.keys = child.keys[0:(t - 1)]
        child.values = child.values[0:(t - 1)]
        if not child.is_leaf:
            z.children = child.children[t:(2 * t)]
            child.children = child.children[0:t]

    def _insert_non_full(self, node: BTreeNode, key: str, value: str):
        i = len(node.keys) - 1
        if node.is_leaf:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            node.keys.insert(i + 1, key)
            node.values.insert(i + 1, value)
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t - 1):
                self._split_child(node, i, node.children[i])
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key, value)
