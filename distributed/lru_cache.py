"""Least Recently Used (LRU) Cache with O(1) get and put."""
from distributed.dlist_node import DListNode

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = DListNode()
        self.tail = DListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: DListNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_front(self, node: DListNode):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: str):
        if key not in self.cache:
            return None
        node = self.cache[key]
        self._remove(node)
        self._add_front(node)
        return node.val

    def put(self, key: str, val: str):
        if key in self.cache:
            self._remove(self.cache[key])
        node = DListNode(key, val)
        self.cache[key] = node
        self._add_front(node)
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
