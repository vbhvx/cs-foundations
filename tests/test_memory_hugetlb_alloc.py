"""Unit test suite for HugeTLB 2MB Large Page Allocator (memory)."""
from memory.hugetlb_alloc import HugetlbAlloc

def test_hugetlb_alloc_lifecycle():
    obj = HugetlbAlloc("test_hugetlb_alloc", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_hugetlb_alloc"
    assert status["capacity"] == 10

def test_hugetlb_alloc_operations():
    obj = HugetlbAlloc("test_hugetlb_alloc_ops", capacity=5)
    ok, res = obj.execute("k1", 100)
    assert ok is True
    assert res == 100
    assert obj.query("k1") == 100
    assert obj.size() == 1
    
    # Overwrite
    ok, res = obj.execute("k1", 200)
    assert ok is True
    assert obj.query("k1") == 200
    assert obj.size() == 1
    
    # Reset
    obj.reset()
    assert obj.size() == 0
