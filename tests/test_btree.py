from storage.btree import BTree

def test_btree():
    bt = BTree(t=2)
    for k in ["d", "b", "a", "c", "e", "f", "g"]:
        bt.insert(k, k.upper())
    assert bt.search("a") == "A"
    assert bt.search("g") == "G"
    assert bt.search("z") is None
