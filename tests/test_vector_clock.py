from distributed.vector_clock import VectorClock

def test_vector_clock():
    vc_a = VectorClock("A")
    vc_b = VectorClock("B")
    msg = vc_a.send()
    vc_b.receive(msg)
    assert VectorClock.compare(msg, vc_b.clock) == "BEFORE"
