from concurrency.treiber_stack import TreiberStack

def test_treiber_stack():
    s = TreiberStack()
    s.push(10)
    s.push(20)
    assert s.pop() == 20
    assert s.pop() == 10
    assert s.pop() is None
