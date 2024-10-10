"""Minimal cooperative coroutine event loop scheduler."""
from collections import deque

class MicroEventLoop:
    def __init__(self):
        self._tasks = deque()

    def add_task(self, generator):
        self._tasks.append(generator)

    def run(self):
        steps = 0
        while self._tasks:
            task = self._tasks.popleft()
            try:
                next(task)
                self._tasks.append(task)
                steps += 1
            except StopIteration:
                pass
        return steps
