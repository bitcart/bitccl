import time

import pytest

from bitccl.events import BaseEvent
from bitccl.exceptions import TimeoutException
from bitccl.utils import no_imports_importer, prepare_event, time_limit


class DummyEvent(BaseEvent):
    name = "dummy_event"


def test_prepare_event():
    assert isinstance(prepare_event("test"), BaseEvent)
    assert isinstance(prepare_event(DummyEvent), DummyEvent)
    assert prepare_event(DummyEvent) == DummyEvent()


def test_no_imports_importer():
    with pytest.raises(ImportError):
        no_imports_importer()


def test_time_limit():
    with time_limit(5):
        pass
    with pytest.raises(TimeoutException):
        with time_limit(1):
            time.sleep(3)
