class BestFit:
    def __init__(self, blocks):
        self.blocks = list(blocks)
    def alloc(self, sz):
        candidates = [(i, b) for i, b in enumerate(self.blocks) if b >= sz]
        if not candidates: return -1
        best_idx = min(candidates, key=lambda x: x[1])[0]
        self.blocks[best_idx] -= sz
        return best_idx
