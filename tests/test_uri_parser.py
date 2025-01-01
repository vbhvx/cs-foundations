from networking.uri_parser import parse_uri

def test_uri_parser():
    u = parse_uri("https://api.github.com/repos?page=1#section")
    assert u.scheme == "https"
    assert u.authority == "api.github.com"
    assert u.path == "/repos"
    assert u.query == "page=1"
    assert u.fragment == "section"
