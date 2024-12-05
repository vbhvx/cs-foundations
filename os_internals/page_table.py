"""Two-level hierarchical page table simulator."""

PAGE_SIZE = 4096
OFFSET_BITS = 12

class TwoLevelPageTable:
    def __init__(self):
        self.directory = {}

    def map_page(self, virtual_addr: int, pfn: int):
        vpn = virtual_addr >> OFFSET_BITS
        pde = (vpn >> 10) & 0x3FF
        pte = vpn & 0x3FF
        if pde not in self.directory:
            self.directory[pde] = {}
        self.directory[pde][pte] = pfn

    def translate(self, virtual_addr: int) -> int:
        vpn = virtual_addr >> OFFSET_BITS
        offset = virtual_addr & 0xFFF
        pde = (vpn >> 10) & 0x3FF
        pte = vpn & 0x3FF
        if pde not in self.directory or pte not in self.directory[pde]:
            raise MemoryError(f"Page fault: 0x{virtual_addr:x}")
        pfn = self.directory[pde][pte]
        return (pfn << OFFSET_BITS) | offset
