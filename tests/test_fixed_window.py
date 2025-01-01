from networking.fixed_window import FixedWindowLimiter
def test_fw(): fw = FixedWindowLimiter(2, 10); assert fw.allow(1); assert fw.allow(2); assert not fw.allow(3)
