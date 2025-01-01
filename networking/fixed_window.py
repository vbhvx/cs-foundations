class FixedWindowLimiter:
    def __init__(self, limit, window):
        self.limit = limit; self.window = window; self.count = 0; self.cur_window = 0
    def allow(self, now):
        w = now // self.window
        if w != self.cur_window: self.cur_window = w; self.count = 0
        if self.count < self.limit: self.count += 1; return True
        return False
