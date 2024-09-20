from concurrency.atomic_ref import AtomicRefCount

def test_atomic_ref():
    ref = AtomicRefCount(1)
    assert ref.inc() == 2
    assert ref.dec() == 1
    assert ref.dec() == 0
