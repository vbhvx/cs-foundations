"""Doubly linked list node for cache eviction structures."""

class DListNode:
    def __init__(self, key: str = "", val: str = ""):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
