import pytest

from bitccl import run


class DummyPlugin:
    def startup(self):
        return {"x": 5}

    def shutdown(self, context):
        pass


class ObjectWithShutdown:
    def __init__(self):
        self.state = True


class DummyPluginWithShutdown:
    def startup(self):
        return {"obj": ObjectWithShutdown()}

    def shutdown(self, context):
        assert context["obj"].state
        context["obj"].state = False


class DummyPluginWithException:
    @classmethod
    def startup(cls):
        return {"y": 1 / 0}

    @classmethod
    def shutdown(cls, context):
        pass


def test_plugin_injection():
    assert run("assert x == 5", plugins=[DummyPlugin()]) is None


def test_plugin_shutdown():
    assert run("assert obj.state", plugins=[DummyPluginWithShutdown()]) is None


def test_plugin_exceptions():
    with pytest.raises(ZeroDivisionError):  # plugins should handle their errors by themselves
        run("assert y", plugins=[DummyPluginWithException])
