"""Lock-free Treiber Stack simulation."""
import threading

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class TreiberStack:
    def __init__(self):
        self._head = None
        self._lock = threading.Lock()

    def push(self, val):
        new_node = Node(val)
        while True:
            with self._lock:
                new_node.next = self._head
                self._head = new_node
                return

    def pop(self):
        while True:
            with self._lock:
                if self._head is None:
                    return None
                val = self._head.val
                self._head = self._head.next
                return val
