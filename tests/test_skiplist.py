from storage.skiplist import SkipList

def test_skiplist():
    sl = SkipList()
    sl.insert("apple", "red")
    sl.insert("banana", "yellow")
    assert sl.get("apple") == "red"
    assert sl.get("banana") == "yellow"
    assert sl.get("cherry") is None
