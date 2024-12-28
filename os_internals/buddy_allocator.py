"""Buddy memory allocation algorithm dividing power-of-two blocks."""

class BuddyAllocator:
    def __init__(self, total_size: int = 1024):
        self.total_size = total_size
        self.free_blocks = {total_size: [0]}

    def allocate(self, size: int) -> int:
        target = 1
        while target < size: target <<= 1
        for blk_size in sorted(self.free_blocks.keys()):
            if blk_size >= target and self.free_blocks[blk_size]:
                addr = self.free_blocks[blk_size].pop(0)
                while blk_size > target:
                    blk_size >>= 1
                    buddy = addr + blk_size
                    if blk_size not in self.free_blocks:
                        self.free_blocks[blk_size] = []
                    self.free_blocks[blk_size].append(buddy)
                return addr
        raise MemoryError("Out of buddy memory")
