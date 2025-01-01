from networking.websocket_frame import parse_ws_frame_header

def test_ws_frame():
    # FIN=1, Opcode=1 (Text), Masked=1, len=5 -> 0x81, 0x85
    info = parse_ws_frame_header(bytes([0x81, 0x85]))
    assert info["fin"] == 1
    assert info["opcode"] == 1
    assert info["masked"] == 1
    assert info["length"] == 5
