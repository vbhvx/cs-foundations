from networking.cookie_jar import CookieJar
def test_cj(): c = CookieJar(); c.set("sid", "123"); assert "sid=123" in c.header()
