"""MemTable in-memory buffer with size threshold tracking."""
from storage.skiplist import SkipList
from storage.skiplist_iter import skiplist_items

TOMBSTONE = "__DELETED__"

class MemTable:
    def __init__(self, max_bytes: int = 1024 * 1024):
        self.max_bytes = max_bytes
        self.current_bytes = 0
        self.skiplist = SkipList()

    def put(self, key: str, value: str):
        self.current_bytes += len(key) + len(value)
        self.skiplist.insert(key, value)

    def delete(self, key: str):
        self.put(key, TOMBSTONE)

    def get(self, key: str):
        val = self.skiplist.get(key)
        if val == TOMBSTONE: return None
        return val

    def is_full(self) -> bool:
        return self.current_bytes >= self.max_bytes

    def items(self):
        return list(skiplist_items(self.skiplist))
