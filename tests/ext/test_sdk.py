"""Our SDK is tested too, so we test only basic integration"""

import pytest
from bitcart import coins

from bitccl import run


@pytest.mark.parametrize("obj", coins.__all__)
def test_scope_exists(obj):
    assert run(obj) is None
    assert run(obj.lower()) is None


@pytest.mark.parametrize("obj", coins.__all__)
def test_anonymous_coins(obj):
    with pytest.warns(UserWarning):
        assert (
            run(f"assert {obj.lower()}.xpub == {obj}().xpub") is None
        )  # ensure lowercase coin names have no xpub set
