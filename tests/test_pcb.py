from os_internals.pcb import Process, ProcessState

def test_pcb():
    p = Process(1, 0, 10)
    assert p.state == ProcessState.NEW
    p.state = ProcessState.READY
    assert p.state == ProcessState.READY
