from concurrency.ticket_lock import TicketLock

def test_ticket_lock():
    tl = TicketLock()
    t = tl.acquire()
    assert t == 0
    tl.release()
    assert tl._now_serving == 1
