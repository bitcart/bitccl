"""HTTPX is well-tested, so we test only the features that are provided by injected http client settings"""
from bitccl import VERSION, run


def test_user_agent():
    assert run(f"assert http.get('http://httpbin.org/user-agent').json() == {{'user-agent': 'bitccl/{VERSION}'}}") is None


def test_http2_enabled():
    assert run("assert http.get('https://nghttp2.org/httpbin/status/200').http_version == 'HTTP/2'") is None


def test_status_codes():
    assert run("assert http_codes.OK == 200") is None
    assert run("assert http_codes.FOUND == 302") is None
    assert run("assert http_codes.BAD_REQUEST == 400") is None
    assert run("assert http_codes.NOT_FOUND == 404") is None
    assert run("assert http_codes.TOO_MANY_REQUESTS == 429") is None
    assert run("assert http_codes.INTERNAL_SERVER_ERROR == 500") is None
