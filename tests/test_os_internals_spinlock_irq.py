"""Unit test suite for Kernel Spinlock with IRQ Disabling (os_internals)."""
from os_internals.spinlock_irq import SpinlockIrq

def test_spinlock_irq_lifecycle():
    obj = SpinlockIrq("test_spinlock_irq", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_spinlock_irq"
    assert status["capacity"] == 10

def test_spinlock_irq_operations():
    obj = SpinlockIrq("test_spinlock_irq_ops", capacity=5)
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
