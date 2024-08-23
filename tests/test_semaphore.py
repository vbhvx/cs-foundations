from concurrency.semaphore import CountingSemaphore
import threading

def test_semaphore():
    sem = CountingSemaphore(2)
    sem.acquire()
    sem.acquire()
    assert sem._value == 0
    sem.release()
    assert sem._value == 1
