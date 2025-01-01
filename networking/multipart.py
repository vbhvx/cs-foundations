def parse_multipart(data, boundary):
    return [p for p in data.split(boundary.encode()) if p.strip() and p != b"--\r\n"]
