"""Unit test suite for RTCP Sender Report Statistic Metric (networking)."""
from networking.rtcp_report import RtcpReport

def test_rtcp_report_lifecycle():
    obj = RtcpReport("test_rtcp_report", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_rtcp_report"
    assert status["capacity"] == 10

def test_rtcp_report_operations():
    obj = RtcpReport("test_rtcp_report_ops", capacity=5)
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
