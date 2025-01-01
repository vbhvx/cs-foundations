from os_internals.alloc_next_fit import NextFit
def test_nf(): nf = NextFit([10, 20]); assert nf.alloc(5) == 0
