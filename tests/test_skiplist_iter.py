from storage.skiplist import SkipList
from storage.skiplist_iter import skiplist_items

def test_skiplist_iteration():
    sl = SkipList()
    for k in ["c", "a", "b"]:
        sl.insert(k, k.upper())
    items = list(skiplist_items(sl))
    assert items == [("a", "A"), ("b", "B"), ("c", "C")]
