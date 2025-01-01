from foundations.sparse_bitset import SparseBitSet

def test_sparse_bitset():
    sbs = SparseBitSet()
    sbs.add(1000000)
    assert sbs.contains(1000000)
    assert not sbs.contains(999999)
