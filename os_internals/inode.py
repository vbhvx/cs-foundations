"""UNIX-style Inode structure with direct and indirect block pointers."""
from typing import List, Optional

BLOCK_SIZE = 512
DIRECT_BLOCKS = 12

class Inode:
    def __init__(self, inode_id: int, is_dir: bool = False):
        self.inode_id = inode_id
        self.is_dir = is_dir
        self.size = 0
        self.direct_blocks: List[int] = []
        self.single_indirect: Optional[int] = None

    def allocate_block(self, block_id: int):
        if len(self.direct_blocks) < DIRECT_BLOCKS:
            self.direct_blocks.append(block_id)
            self.size += BLOCK_SIZE
        else:
            raise NotImplementedError("Indirect block allocation needed")
