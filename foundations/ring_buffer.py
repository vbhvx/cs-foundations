"""Fixed-capacity circular ring buffer."""

class RingBuffer:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def push(self, val):
        self.buffer[self.tail] = val
        self.tail = (self.tail + 1) % self.capacity
        if self.size < self.capacity:
            self.size += 1
        else:
            self.head = (self.head + 1) % self.capacity

    def pop(self):
        if self.size == 0: raise IndexError("Buffer empty")
        val = self.buffer[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return val
