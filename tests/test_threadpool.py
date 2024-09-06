from concurrency.threadpool import ThreadPool

def test_threadpool():
    pool = ThreadPool(2)
    f1 = pool.submit(lambda x: x * 2, 21)
    f2 = pool.submit(lambda x, y: x + y, 10, 20)
    assert f1.result(timeout=2.0) == 42
    assert f2.result(timeout=2.0) == 30
    pool.shutdown()
