from secrets import token_urlsafe

import pytest

from bitccl.functions import (
    add_event_listener,
    dispatch_event,
    on,
    password,
    send_email,
)
from bitccl.functions import template as template_f
from bitccl.state import event_listeners


def test_password():
    assert len(token_urlsafe()) == len(password())  # maintain secure defaults
    assert isinstance(password(), str)
    for password_len in range(0, 128 + 1):
        assert len(password(password_len)) == password_len


def test_template(template):
    assert template_f("notfound") == ""
    assert template_f(template) == "Hello !"
    assert template_f(template, {"name": "world"}) == "Hello world!"
    assert template_f(template, {"name": "test"}) == "Hello test!"


def test_add_event_listener(prepared_event):
    assert event_listeners == {}
    add_event_listener("test", lambda: None)
    assert len(event_listeners[prepared_event]) == 1
    add_event_listener("test", lambda: None)
    assert len(event_listeners[prepared_event]) == 2


def test_on_decorator(prepared_event):
    assert len(event_listeners[prepared_event]) == 2

    @on("test")
    def func():  # pylint:disable=unused-variable
        return 4 / 0

    assert len(event_listeners[prepared_event]) == 3


def test_dispatch_event(prepared_event):
    dispatch_event("test")  # no exception raised
    dispatch_event(prepared_event)  # same event as test
    dispatch_event("notexist")  # always silent


@pytest.mark.slow
def test_send_email():
    assert not send_email("test@test.com", "Test", "Test")  # not configured
    # TODO: find a way to test email sending
