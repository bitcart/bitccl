from bitccl import run
from bitccl.state import config, event_listeners


def test_config_singleton():
    assert config.get() == {}
    config.set({"test": 1})
    assert config.get() == config.get() == {"test": 1}  # consistent
    assert config.get().test == 1
    config.set({})
    assert config.get() == {}


def test_empty_event_listeners():
    event_listeners.clear()
    assert not event_listeners
    assert run("add_event_listener('test', lambda:None)") is None  # no errors
    assert not event_listeners  # cleanup after run
