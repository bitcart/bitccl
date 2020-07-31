import pytest
from bitccl import run, functions, events


def test_run():
    assert run("a = 2+2") is None  # no output if no errors
    error_message = run("a = 2 / 0")
    assert error_message
    assert "ZeroDivisionError" in error_message
    import os  # noqa # imports working after run function finalization


def test_disable_imports():
    assert "Imports disabled" in run("import pdb")


@pytest.mark.parametrize("func", [
    "template",
    "send_email",
])
def test_allowed_imports(func):
    assert run(f'from .functions import{func}') is None


@pytest.mark.parametrize("func", [
    "add_event_listener",
    "on",
    "dispatch_event",
    "password",
])
def test_disallowed_imports(func):
    assert "Imports disabled" in run(f"from functions import {func}")


def test_builtin_functions():
    for name, func in functions.items():
        assert run(f'assert "function" in str(type({name}))') is None


def test_builtin_events():
    for name, event in events.items():
        assert run(f'assert "class" in str({name})') is None
