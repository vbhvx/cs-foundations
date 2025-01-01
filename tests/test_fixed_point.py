from foundations.fixed_point import FixedPoint

def test_fixed_point():
    a = FixedPoint(1.2345)
    b = FixedPoint(2.3456)
    c = a + b
    assert abs(c.to_float() - 3.5801) < 1e-4
