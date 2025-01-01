"""HTTP/1.1 response builder and wire formatter."""

STATUS_TEXTS = {200: "OK", 400: "Bad Request", 404: "Not Found", 500: "Internal Server Error"}

class HTTPResponse:
    def __init__(self, status_code: int = 200, headers: dict = None, body: bytes = b""):
        self.status_code = status_code
        self.headers = headers or {}
        self.body = body

    def to_bytes(self) -> bytes:
        text = STATUS_TEXTS.get(self.status_code, "Unknown")
        lines = [f"HTTP/1.1 {self.status_code} {text}"]
        hdrs = dict(self.headers)
        if "content-length" not in hdrs and self.body:
            hdrs["Content-Length"] = str(len(self.body))
        for k, v in hdrs.items():
            lines.append(f"{k}: {v}")
        header_part = "\r\n".join(lines).encode("iso-8859-1") + b"\r\n\r\n"
        return header_part + self.body
