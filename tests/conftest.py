import pytest

from bitccl.state import config as config_ctx
from bitccl.utils import prepare_event


@pytest.fixture(autouse=True)
def config():
    config_ctx.set({})


@pytest.fixture
def template():
    with open("templates/test.j2", "w") as f:
        f.write("Hello {{name}}!")
    return "test"


@pytest.fixture
def prepared_event():
    return prepare_event("test")
