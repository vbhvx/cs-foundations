from concurrency.bounded_semaphore import BoundedSemaphore
import pytest

def test_bounded_semaphore():
    sem = BoundedSemaphore(1)
    with pytest.raises(ValueError):
        sem.release()
