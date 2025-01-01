from networking.frame import encode_frame
from networking.frame_stream import FrameStreamDecoder

def test_frame_stream():
    stream = FrameStreamDecoder()
    f = encode_frame(2, b"chunked payload")
    stream.feed(f[:5])
    assert stream.pop_frame() is None
    stream.feed(f[5:])
    res = stream.pop_frame()
    assert res == (2, b"chunked payload")
