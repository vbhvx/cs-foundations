from networking.frame import encode_frame, decode_frame
import pytest

def test_frame():
    f = encode_frame(1, b"ping")
    m_type, payload = decode_frame(f)
    assert m_type == 1
    assert payload == b"ping"
    with pytest.raises(ValueError):
        decode_frame(b"bad magic")
