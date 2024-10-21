from concurrency.priority_mutex import PriorityMutex

def test_priority_mutex():
    m = PriorityMutex()
    m.acquire(10)
    assert m.holding_priority == 10
    m.release()
    assert m.holding_priority == 0
