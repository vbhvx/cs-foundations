from os_internals.inode import Inode

def test_inode_allocation():
    ino = Inode(1)
    ino.allocate_block(101)
    assert len(ino.direct_blocks) == 1
    assert ino.size == 512
