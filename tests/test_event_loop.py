from concurrency.event_loop import MicroEventLoop

def test_micro_event_loop():
    loop = MicroEventLoop()
    log = []
    def task1():
        log.append("1a")
        yield
        log.append("1b")
    def task2():
        log.append("2a")
        yield
        log.append("2b")
    loop.add_task(task1())
    loop.add_task(task2())
    loop.run()
    assert log == ["1a", "2a", "1b", "2b"]
