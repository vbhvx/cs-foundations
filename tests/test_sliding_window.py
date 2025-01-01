from networking.sliding_window import GoBackN

def test_go_back_n():
    gbn = GoBackN(3)
    assert gbn.send("pkt0")
    assert gbn.send("pkt1")
    assert gbn.send("pkt2")
    assert not gbn.send("pkt3")  # Window full
    gbn.ack(1)  # Cumulative ACK up to 1
    assert gbn.base == 2
    assert gbn.send("pkt3")
