import pytest

from bitccl.state import config as config_ctx
from bitccl.utils import prepare_event


@pytest.fixture(autouse=True)
def config():
    config_ctx.set({})


def pytest_addoption(parser):
    parser.addoption("--runslow", action="store_true", default=False, help="run slow tests")


def pytest_configure(config):
    config.addinivalue_line("markers", "slow: mark test as slow to run")


def pytest_collection_modifyitems(config, items):
    if config.getoption("--runslow"):
        # --runslow given in cli: do not skip slow tests
        return
    skip_slow = pytest.mark.skip(reason="need --runslow option to run")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)


@pytest.fixture
def template():
    with open("templates/test.j2", "w") as f:
        f.write("Hello {{name}}!")
    return "test"


@pytest.fixture
def prepared_event():
    return prepare_event("test")
