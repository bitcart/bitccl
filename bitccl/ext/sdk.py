import warnings

from bitcart import COINS


def startup():
    context = {}
    with warnings.catch_warnings():  # for coins init without xpub
        warnings.simplefilter("ignore")
        for coin_name, coin_class in COINS.items():
            context[coin_name] = coin_class
            context[coin_name.lower()] = coin_class()
    return context


def shutdown(context):
    pass
