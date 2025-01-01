from networking.http_response import HTTPResponse

def test_http_response():
    res = HTTPResponse(200, {"Content-Type": "text/plain"}, b"Hello Systems")
    wire = res.to_bytes()
    assert wire.startswith(b"HTTP/1.1 200 OK\r\n")
    assert b"Content-Length: 13" in wire
    assert wire.endswith(b"Hello Systems")
