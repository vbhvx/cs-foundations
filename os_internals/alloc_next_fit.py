class NextFit:
    def __init__(self, blocks):
        self.blocks = list(blocks)
        self.last = 0
    def alloc(self, sz):
        n = len(self.blocks)
        for i in range(n):
            idx = (self.last + i) % n
            if self.blocks[idx] >= sz:
                self.blocks[idx] -= sz
                self.last = idx
                return idx
        return -1
