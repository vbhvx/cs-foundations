from concurrency.future import Future
import pytest

def test_future_result():
    f = Future()
    f.set_result(42)
    assert f.result() == 42

def test_future_exception():
    f = Future()
    f.set_exception(ValueError("Test Error"))
    with pytest.raises(ValueError):
        f.result()
