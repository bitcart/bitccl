import io
from contextlib import redirect_stdout

import pytest

from bitccl.events import BaseEvent
from bitccl.functions import add_event_listener, dispatch_event
from bitccl.state import event_listeners


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
    assert event2.name == "dummy"  # pylint: disable=no-member # pylint bug
    assert event2.args_len == event2.required_len == 1
    assert event2.parsed_args == [1]
    assert repr(event2) == "dummy event parsed_args=[1]"
    with pytest.raises(AttributeError):  # no name set
        repr(event)

    def handler(test):
        print("test", test)

    add_event_listener(event2, handler)
    f1 = io.StringIO()
    f2 = io.StringIO()
    with redirect_stdout(f1):
        dispatch_event(event2)
    with redirect_stdout(f2):
        event2.dispatch()
    assert f1.getvalue() == f2.getvalue() == "test 1\n"
    del event_listeners[event2]
