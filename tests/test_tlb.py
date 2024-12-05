from os_internals.tlb import TLB

def test_tlb():
    tlb = TLB(2)
    assert tlb.lookup(1) is None
    assert tlb.misses == 1
    tlb.insert(1, 100)
    assert tlb.lookup(1) == 100
    assert tlb.hits == 1
