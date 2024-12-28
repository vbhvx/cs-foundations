from os_internals.buddy_allocator import BuddyAllocator

def test_buddy_alloc():
    ba = BuddyAllocator(1024)
    addr = ba.allocate(100)
    assert addr == 0
