import pytest

from bitccl import events, functions, run


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
        assert run(f'assert "function" in str(type({name}))') is None


def test_builtin_events():
    for name in events:
        assert run(f'assert "class" in str({name})') is None
        assert run(f"assert issubclass({name}, BaseEvent)") is None
