"""HTTP wire parsing throughput benchmark."""
from networking.http_request import parse_http_request
from benchmarks.harness import time_execution

RAW_REQ = b"GET /api/v1/resource HTTP/1.1\r\nHost: example.com\r\nAccept: */*\r\n\r\n"

def bench_http_parser():
    return time_execution(lambda: parse_http_request(RAW_REQ), 500)
