from foundations.bits import popcount_naive, popcount_brian_kernighan
def test_popcount():
    assert popcount_naive(0) == 0
    assert popcount_brian_kernighan(0) == 0
    assert popcount_naive(0b101101) == 4
    assert popcount_brian_kernighan(0b101101) == 4
