"""SkipList node with forward pointers at multiple levels."""

class SkipListNode:
    def __init__(self, key: str, value: str, level: int):
        self.key = key
        self.value = value
        self.forward = [None] * level
