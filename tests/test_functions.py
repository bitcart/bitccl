from bitccl.functions import password
from secrets import token_urlsafe


def test_password():
    assert len(token_urlsafe()) == len(password())  # maintain secure defaults
    assert isinstance(password(), str)
    for password_len in range(0, 128 + 1):
        assert len(password(password_len)) == password_len
