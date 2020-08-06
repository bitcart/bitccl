import warnings

from bitcart import coins

from ..utils import mark_allowed_imports


def startup():
    context = {}
    with warnings.catch_warnings():  # for coins init without xpub
        warnings.simplefilter("ignore")
        for coin_name in coins.__all__:
            coin_class = getattr(coins, coin_name)
            context[coin_name] = mark_allowed_imports(coin_class)
            context[coin_name.lower()] = mark_allowed_imports(coin_class())
    return context


def shutdown(context):
    pass
