from foundations.ring_buffer import RingBuffer

def test_ring_buffer():
    rb = RingBuffer(3)
    rb.push(1); rb.push(2); rb.push(3)
    assert rb.pop() == 1
    rb.push(4)
    assert rb.pop() == 2
