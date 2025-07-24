"""Unit test suite for MQTT Connect & Publish Packet Parser (networking)."""
from networking.mqtt_codec import MqttCodec

def test_mqtt_codec_lifecycle():
    obj = MqttCodec("test_mqtt_codec", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_mqtt_codec"
    assert status["capacity"] == 10

def test_mqtt_codec_operations():
    obj = MqttCodec("test_mqtt_codec_ops", capacity=5)
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
