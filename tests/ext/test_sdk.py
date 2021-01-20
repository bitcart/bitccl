"""Our SDK is tested too, so we test only basic integration"""

import pytest
from bitcart import COINS

from bitccl import run


@pytest.mark.parametrize("obj", COINS)
def test_scope_exists(obj):
    assert run(obj) is None
    assert run(obj.lower()) is None
