from bitccl import run


def test_run():
    assert run("a = 2+2") is None  # no output if no errors
    error_message = run("a = 2 / 0")
    assert error_message
    assert "ZeroDivisionError" in error_message
    import os  # noqa # imports working after run function finalization
