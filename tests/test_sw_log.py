from networking.sliding_window_log import SlidingWindowLog
def test_swl(): sw = SlidingWindowLog(2, 10); assert sw.allow(1); assert sw.allow(2); assert not sw.allow(3)
