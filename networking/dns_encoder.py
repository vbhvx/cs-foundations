"""RFC 1035 DNS question wire format encoder."""
import struct

def encode_dns_query(domain: str, tx_id: int = 0x1234) -> bytes:
    header = struct.pack(">HHHHHH", tx_id, 0x0100, 1, 0, 0, 0)
    question = bytearray()
    for part in domain.split("."):
        question.append(len(part))
        question.extend(part.encode("ascii"))
    question.append(0)  # null root
    question.extend(struct.pack(">HH", 1, 1))  # QTYPE A, QCLASS IN
    return header + bytes(question)
