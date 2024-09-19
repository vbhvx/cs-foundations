"""Michael-Scott two-lock / atomic queue simulation."""
import threading

class QueueNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class MSQueue:
    def __init__(self):
        dummy = QueueNode()
        self._head = dummy
        self._tail = dummy
        self._h_lock = threading.Lock()
        self._t_lock = threading.Lock()

    def enqueue(self, val):
        node = QueueNode(val)
        with self._t_lock:
            self._tail.next = node
            self._tail = node

    def dequeue(self):
        with self._h_lock:
            node = self._head
            new_head = node.next
            if new_head is None:
                return None
            val = new_head.val
            new_head.val = None
            self._head = new_head
            return val
