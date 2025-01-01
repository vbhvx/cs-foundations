from networking.http_request import parse_http_request

def test_parse_http_request():
    raw = b"GET /index.html HTTP/1.1\r\nHost: localhost\r\nUser-Agent: test\r\n\r\n"
    req = parse_http_request(raw)
    assert req.method == "GET"
    assert req.path == "/index.html"
    assert req.headers["host"] == "localhost"
