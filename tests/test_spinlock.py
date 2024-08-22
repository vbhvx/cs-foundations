from concurrency.spinlock import SpinLock
import threading

def test_spinlock_mutual_exclusion():
    lock = SpinLock()
    counter = 0
    def worker():
        nonlocal counter
        for _ in range(100):
            with lock:
                counter += 1
    threads = [threading.Thread(target=worker) for _ in range(5)]
    for t in threads: t.start()
    for t in threads: t.join()
    assert counter == 500
