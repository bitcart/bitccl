import io
from contextlib import redirect_stdout

import pytest

from bitccl.compiler import events
from bitccl.events import BaseEvent
from bitccl.functions import add_event_listener, dispatch_event
from bitccl.state import event_listeners

# Test util


def camel_to_snake_case(s):
    return "".join(["_" + c.lower() if c.isupper() else c for c in s]).lstrip("_")


# tests


class DummyEvent(BaseEvent):
    name = "dummy"
    required_len = 1
    args_len = 1


def test_base_event():
    assert BaseEvent._dispatch_event  # event dispatching loaded
    event = BaseEvent()  # no exception raised
    assert not hasattr(event, "name")  # base class
    with pytest.raises(AttributeError):  # no name set
        BaseEvent(1)
    with pytest.raises(TypeError):
        DummyEvent()
    with pytest.raises(TypeError):
        DummyEvent(1, 2)
    event2 = DummyEvent(1)
    assert event2.name == "dummy"
    assert event2.args_len == event2.required_len == 1
    assert event2.parsed_args == [1]
    assert repr(event2) == "dummy event parsed_args=[1]"
    with pytest.raises(AttributeError):  # no name set
        repr(event)

    def handler(test):
        print("test", test)

    async def async_handler(test):
        print("asynctest", test)

    add_event_listener(event2, handler)
    add_event_listener(event2, async_handler)
    f1 = io.StringIO()
    f2 = io.StringIO()
    with redirect_stdout(f1):
        dispatch_event(event2)
    with redirect_stdout(f2):
        event2.dispatch()
    assert f1.getvalue() == f2.getvalue() == "test 1\nasynctest 1\n"
    del event_listeners[event2]


@pytest.mark.parametrize("event", events.values())
def test_event_names(event):
    if event != BaseEvent:
        assert event.name == camel_to_snake_case(event.__name__)  # to avoid typos
