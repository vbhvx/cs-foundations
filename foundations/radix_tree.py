"""Radix Tree for routing tables and longest prefix matching."""

class RadixNode:
    def __init__(self, prefix: str = ""):
        self.prefix = prefix
        self.children = {}
        self.value = None

class RadixTree:
    def __init__(self):
        self.root = RadixNode()

    def insert(self, key: str, value):
        cur = self.root
        for ch in key:
            if ch not in cur.children:
                cur.children[ch] = RadixNode(ch)
            cur = cur.children[ch]
        cur.value = value

    def longest_prefix_match(self, key: str):
        cur = self.root
        match = None
        for ch in key:
            if ch not in cur.children: break
            cur = cur.children[ch]
            if cur.value is not None:
                match = cur.value
        return match
