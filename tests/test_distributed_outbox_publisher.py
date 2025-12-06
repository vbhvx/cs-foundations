"""Unit test suite for Outbox Pattern Reliable Event Publisher (distributed)."""
from distributed.outbox_publisher import OutboxPublisher

def test_outbox_publisher_lifecycle():
    obj = OutboxPublisher("test_outbox_publisher", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_outbox_publisher"
    assert status["capacity"] == 10

def test_outbox_publisher_operations():
    obj = OutboxPublisher("test_outbox_publisher_ops", capacity=5)
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
