<p align="center">
  <a href="https://bitcartcc.com"><img src="https://raw.githubusercontent.com/bitcartcc/bitccl/master/logo.png" alt="BitCCL"></a>
</p>

---
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/bitcartcc/bitccl/test?style=flat-square)
![Codecov](https://img.shields.io/codecov/c/github/bitcartcc/bitccl?style=flat-square)
![PyPI](https://img.shields.io/pypi/v/bitccl?style=flat-square)
![PyPI - Downloads](https://img.shields.io/pypi/dm/bitccl?style=flat-square)

---

BitCCL is a [BitcartCC](https://bitcartcc.com) scripting language used for automating checkout flow and more.

It is currently in alpha stage, being separated from the [main BitcartCC repository](https://github.com/bitcartcc/bitcart).

## Architechture

BitCCL is basically Python, but:
- Safe, with disabled import system
- Robust, with many built-in functions
- Optimized for running in BitcartCC environment

Language file extension is `.bccl`.

## Running

```
pip install -r requirements.txt
./compiler example.bitccl
```

## Built-in functions

Current built-in functions list can be always seen in `functions.py` file.

Table of built-in functions:

| Signature                                | Description                                                                                                                                     | Return value                                         | Imports allowed |
|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|-----------------|
| `add_event_listener(event, func)`        | Adds event listener `func` to be called when `event` is dispatched                                                                              | None                                                 | :x:             |
| `@on(event)`                             | A decorator used for registering functions to be called when `event` is dispatched. Example: ``` @on(ProductBought(1)) def func():     pass ``` | Wrapper function                                     | :x:             |
| `dispatch_event(event, *args, **kwargs)` | Dispatch `event`, optionally passing positional or named arguments to event handlers                                                            | None                                                 | :x:             |
| `template(name, data={})`                | Render template `name`, optionally passing `data` to it                                                                                         | Template text on success, empty string("") otherwise | :heavy_check_mark:             |
| `send_email(to, subject, text)`          | Sends email to email address `to`, with `subject` and `text`. Uses email server configuration from `config.json`                                | True on success, False otherwise                     | :heavy_check_mark:             |
| `password(length=SECURE_PASSWORD_LENGTH)`                  | Generate cryptographically unique password of `length` if provided, otherwise uses safe enough length.                                          | Generated password                                   | :x:             |

Also a http client is available.

To send http request with it, use:

`http.method(url)`

To send HTTP method (get, post, delete, patch, etc.) to url.
You can also optionally pass additional query parameters (params argument), request body data (data argument), 
files (files argument), headers (headers argument), cookies (cookie argument) and more.

Here is how the most complex request might look like:

```python
http.method(url, params={}, headers={}, cookies={}, auth=None, allow_redirects=True, cert="", verify=True, timeout=5.0)
```

All arguments except for url are optional.

After sending a request, you can retrieve response data:

If res is response got from calling `http.method(...)`, then:

`res.text` will return text data from response (for example, html)

`res.content` will return binary data from response (for example, file contents)

`res.json()` will return json data from response (for example, when accessing different web APIs)

Response status code can be got as `res.status_code`.

For convenience, you are provided with http request codes to easily check if request is successful without remembering the numbers.

For example, `http_codes.OK` is status code 200 (success).
So, to check if request has succeeded, you can check like so:

```python
res = http.get("https://example.com")
if res.status_code == http_codes.OK:
    print("Success")
```

For additional information about built-in http client, you can read it's full [documentation](https://www.python-httpx.org/quickstart)

Also, [BitcartCC SDK](https://sdk.bitcartcc.com) is available to use.

To access coins without xpub to get transaction, fiat rate or anything else not requiring a wallet, you can access each coin by
it's lowercase symbol, for example:

```python
print(btc.rate())
print(ltc.rate())
print(bch.rate())
print(gzro.rate())
print(bsty.rate())
```

**Note**: running coins' commands require it's daemon running if you are not using BitCCL from BitcartCC deployment.

To perform operations requiring a wallet, use upper-case coin symbol, passing xpub/ypub/zpub/xprv/yprv/zprv/electrum seed in it:

```python
coin = BTC(xpub="my xpub")
print(coin.balance())
# or if using only once:
print(BTC(xpub="my xpub").balance())
```

## Built-in events 

Refer to [events.md](events.md).

It is generated automatically from BitCCL code.

## Plugin system

If using BitCCL programmatically, you can extend it's execution context with plugins.

Pass a list of plugin-like objects to `run` function, like so:

```python
from bitccl import run

run("print(x)", plugins=[TestPlugin()])
```

Each plugin can be anything: class, object, module object, it must have two methods:

`startup()` method returning dictionary, which will be used to update execution context with new variables

`shutdown(context)` method which should perform a clean-up of injected variables if needed

Here's TestPlugin code from above's example:

```python
class TestPlugin:
    def startup(self):
        return {"x": 5}

    def shutdown(self, context):
        pass
```

## Contributing

You can contribute to BitCCL language by suggesting new built-in functions and events to be added, as well as any ideas for improving it.
Open an [issue](https://github.com/bitcartcc/bitccl/issues/new/choose) to suggest new features

Also see our [contributing guidelines](CONTRIBUTING.md).

## Copyright and License

Copyright (C) 2020 MrNaif2018

Licensed under the [LGPLv3+](LICENSE)