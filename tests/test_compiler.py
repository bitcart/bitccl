import io
from contextlib import redirect_stdout

import pytest

from bitccl import run
from bitccl.compiler import events, functions

CLASS_TEST = """
class Test:
    def __init__(self, x):
        self.x = x
    def do_it(self):
        return self.x

test = Test(5)
assert test.do_it() == 5
"""

DYNATTRS_TEST = """
class Test:
    def __init__(self, x):
        self.x = x

assert not hasattr(Test, "x")
test = Test(5)
assert hasattr(test, "x")
assert getattr(test,"x") == 5
assert getattr(Test,"x", "default") == "default"
"""

CALL_ARGS_KWARGS_TEST = """
def func(*args, **kwargs):
    assert args == (5,)
    assert kwargs == {"test": "value"}

func(*[5], **{"test":"value"})
"""


def test_run():
    assert run("a = 2+2") is None  # no output if no errors
    error_message = run("a = 2 / 0")
    assert error_message
    assert "ZeroDivisionError" in error_message
    import os  # noqa # imports working after run function finalization


def test_disable_imports():
    assert "Imports disabled" in run("import pdb")


@pytest.mark.parametrize("func", functions.keys())
def test_disallowed_imports(func):
    assert "Imports disabled" in run(f"from functions import {func}")


def test_builtin_functions():
    for name in functions:
        assert run(f"assert {name}") is None


def test_builtin_events():
    for name in events:
        assert run(f'assert "class" in str({name})') is None
        assert run(f"assert issubclass({name}, BaseEvent)") is None


def test_print_works():
    f = io.StringIO()
    with redirect_stdout(f):
        assert run("print(5)") is None
    assert f.getvalue().strip() == "5"


def test_class_works():
    assert run(CLASS_TEST) is None


def test_inplace_ops():
    assert run("a = 5; a += 2; assert a == 7") is None


def test_dynamic_attributes():
    assert run(DYNATTRS_TEST) is None


def test_call_args_kwargs():
    assert run(CALL_ARGS_KWARGS_TEST) is None
