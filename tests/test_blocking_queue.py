from concurrency.blocking_queue import BoundedBlockingQueue
import threading

def test_blocking_queue():
    q = BoundedBlockingQueue(5)
    results = []
    def consumer():
        for _ in range(10):
            results.append(q.get())
    t = threading.Thread(target=consumer)
    t.start()
    for i in range(10): q.put(i)
    t.join()
    assert results == list(range(10))
