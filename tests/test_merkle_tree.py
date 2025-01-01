from distributed.merkle_tree import MerkleTree

def test_merkle_tree():
    t1 = MerkleTree(["tx1", "tx2", "tx3", "tx4"])
    t2 = MerkleTree(["tx1", "tx2", "tx3", "tx4"])
    assert t1.root() == t2.root()
    t3 = MerkleTree(["tx1", "tx2", "tx3", "tx_tampered"])
    assert t1.root() != t3.root()
