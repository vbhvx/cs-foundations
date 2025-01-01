"""HTTP/1.1 request line and header parser."""

class HTTPRequest:
    def __init__(self, method: str, path: str, version: str, headers: dict, body: bytes = b""):
        self.method = method
        self.path = path
        self.version = version
        self.headers = headers
        self.body = body

def parse_http_request(raw: bytes) -> HTTPRequest:
    lines = raw.split(b"\r\n")
    start_line = lines[0].decode("ascii").split()
    if len(start_line) != 3: raise ValueError("Invalid HTTP start line")
    method, path, version = start_line
    headers = {}
    i = 1
    while i < len(lines) and lines[i]:
        line = lines[i].decode("iso-8859-1")
        k, v = line.split(":", 1)
        headers[k.strip().lower()] = v.strip()
        i += 1
    body = b"\r\n".join(lines[i+1:]) if i < len(lines) else b""
    return HTTPRequest(method, path, version, headers, body)
