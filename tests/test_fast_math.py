from foundations.fast_math import fast_pow
def test_fast_pow():
    assert fast_pow(2, 10) == 1024 and fast_pow(2, 10, 1000) == 24
