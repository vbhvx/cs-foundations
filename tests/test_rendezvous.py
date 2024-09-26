from concurrency.rendezvous import RendezvousChannel
import threading

def test_rendezvous():
    ch = RendezvousChannel()
    res = []
    def sender(): ch.send(99)
    t = threading.Thread(target=sender)
    t.start()
    val = ch.receive()
    t.join()
    assert val == 99
