class WorstFit:
    def __init__(self, blocks):
        self.blocks = list(blocks)
    def alloc(self, sz):
        max_idx = max(range(len(self.blocks)), key=lambda i: self.blocks[i])
        if self.blocks[max_idx] >= sz:
            self.blocks[max_idx] -= sz
            return max_idx
        return -1
