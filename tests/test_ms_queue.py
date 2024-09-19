from concurrency.ms_queue import MSQueue

def test_ms_queue():
    q = MSQueue()
    q.enqueue("A")
    q.enqueue("B")
    assert q.dequeue() == "A"
    assert q.dequeue() == "B"
    assert q.dequeue() is None
