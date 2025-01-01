"""In-memory SkipList implementation for O(log n) ordered key-value operations."""
import random
from storage.skiplist_node import SkipListNode

MAX_LEVEL = 16
P = 0.5

class SkipList:
    def __init__(self):
        self.head = SkipListNode("", "", MAX_LEVEL)
        self.level = 1
        self.size = 0

    def _random_level(self) -> int:
        lvl = 1
        while random.random() < P and lvl < MAX_LEVEL:
            lvl += 1
        return lvl

    def insert(self, key: str, value: str):
        update = [None] * MAX_LEVEL
        cur = self.head
        for i in reversed(range(self.level)):
            while cur.forward[i] and cur.forward[i].key < key:
                cur = cur.forward[i]
            update[i] = cur
        cur = cur.forward[0]
        if cur and cur.key == key:
            cur.value = value
            return
        lvl = self._random_level()
        if lvl > self.level:
            for i in range(self.level, lvl):
                update[i] = self.head
            self.level = lvl
        new_node = SkipListNode(key, value, lvl)
        for i in range(lvl):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node
        self.size += 1

    def get(self, key: str):
        cur = self.head
        for i in reversed(range(self.level)):
            while cur.forward[i] and cur.forward[i].key < key:
                cur = cur.forward[i]
        cur = cur.forward[0]
        if cur and cur.key == key:
            return cur.value
        return None
