"""Forward iterator over SkipList items."""
from storage.skiplist import SkipList

def skiplist_items(sl: SkipList):
    cur = sl.head.forward[0]
    while cur:
        yield cur.key, cur.value
        cur = cur.forward[0]
