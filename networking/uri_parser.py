"""RFC 3986 URI parsing implementation."""
import re

URI_PATTERN = re.compile(r"^(?:([^:/?#]+):)?(?://([^/?#]*))?([^?#]*)(?:\?([^#]*))?(?:#(.*))?$")

class ParsedURI:
    def __init__(self, scheme, authority, path, query, fragment):
        self.scheme = scheme
        self.authority = authority
        self.path = path or "/"
        self.query = query
        self.fragment = fragment

def parse_uri(raw_uri: str) -> ParsedURI:
    m = URI_PATTERN.match(raw_uri)
    if not m: raise ValueError("Invalid URI")
    scheme, auth, path, query, frag = m.groups()
    return ParsedURI(scheme, auth, path, query, frag)
