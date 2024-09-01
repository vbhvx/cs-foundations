from concurrency.barrier import CyclicBarrier
import threading

def test_barrier():
    b = CyclicBarrier(3)
    phase_reached = []
    def worker():
        b.wait()
        phase_reached.append(1)
    threads = [threading.Thread(target=worker) for _ in range(2)]
    for t in threads: t.start()
    assert len(phase_reached) == 0
    b.wait()
    for t in threads: t.join()
    assert len(phase_reached) == 2
