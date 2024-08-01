from foundations.fnv_hash import fnv1a_32
def test_fnv1a():
    assert fnv1a_32(b"") == 0x811c9dc5
    assert fnv1a_32(b"hello") != fnv1a_32(b"world")
