"""Process Control Block representation and state transitions."""
from enum import Enum, auto

class ProcessState(Enum):
    NEW = auto()
    READY = auto()
    RUNNING = auto()
    WAITING = auto()
    TERMINATED = auto()

class Process:
    def __init__(self, pid: int, arrival_time: int, burst_time: int, priority: int = 0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.priority = priority
        self.state = ProcessState.NEW
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0
