"""Go-Back-N sliding window flow control model."""

class GoBackN:
    def __init__(self, window_size: int):
        self.window_size = window_size
        self.base = 0
        self.next_seq = 0
        self.buffer = {}

    def send(self, data) -> bool:
        if self.next_seq < self.base + self.window_size:
            self.buffer[self.next_seq] = data
            self.next_seq += 1
            return True
        return False

    def ack(self, ack_num: int):
        if ack_num >= self.base:
            for i in range(self.base, ack_num + 1):
                self.buffer.pop(i, None)
            self.base = ack_num + 1
