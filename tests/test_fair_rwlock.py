from concurrency.fair_rwlock import FairReadWriteLock

def test_fair_rwlock():
    rw = FairReadWriteLock()
    rw.acquire_read()
    assert rw._active_readers == 1
    rw.release_read()
    assert rw._active_readers == 0
