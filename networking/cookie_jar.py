class CookieJar:
    def __init__(self): self.cookies = {}
    def set(self, k, v): self.cookies[k] = v
    def header(self): return "; ".join(f"{k}={v}" for k, v in self.cookies.items())
