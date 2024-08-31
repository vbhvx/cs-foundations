from concurrency.rwlock import ReadWriteLock

def test_rwlock():
    rw = ReadWriteLock()
    rw.acquire_read()
    rw.acquire_read()
    assert rw._readers == 2
    rw.release_read()
    rw.release_read()
    rw.acquire_write()
    assert rw._writer_active
    rw.release_write()
