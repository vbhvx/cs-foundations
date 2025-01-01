from networking.multipart import parse_multipart
def test_mp(): assert len(parse_multipart(b"--bound\r\npart1\r\n--bound", "bound")) >= 1
