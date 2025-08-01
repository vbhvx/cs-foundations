"""Unit test suite for Ticket Spinlock with FIFO Grant (concurrency)."""
from concurrency.ticket_spinlock import TicketSpinlock

def test_ticket_spinlock_lifecycle():
    obj = TicketSpinlock("test_ticket_spinlock", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_ticket_spinlock"
    assert status["capacity"] == 10

def test_ticket_spinlock_operations():
    obj = TicketSpinlock("test_ticket_spinlock_ops", capacity=5)
    ok, res = obj.execute("k1", 100)
    assert ok is True
    assert res == 100
    assert obj.query("k1") == 100
    assert obj.size() == 1
    
    # Overwrite
    ok, res = obj.execute("k1", 200)
    assert ok is True
    assert obj.query("k1") == 200
    assert obj.size() == 1
    
    # Reset
    obj.reset()
    assert obj.size() == 0
