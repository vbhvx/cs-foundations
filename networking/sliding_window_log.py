class SlidingWindowLog:
    def __init__(self, limit, window):
        self.limit = limit; self.window = window; self.log = []
    def allow(self, now):
        self.log = [t for t in self.log if now - t < self.window]
        if len(self.log) < self.limit:
            self.log.append(now); return True
        return False
