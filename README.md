<p align="center">
  <a href="https://bitcartcc.com"><img src="https://raw.githubusercontent.com/MrNaif2018/bitccl/master/logo.png" alt="BitCCL"></a>
</p>

---
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/MrNaif2018/bitccl/test?style=flat-square)
![Codecov](https://img.shields.io/codecov/c/github/MrNaif2018/bitccl?style=flat-square)
![PyPI](https://img.shields.io/pypi/v/bitccl?style=flat-square)
![PyPI - Downloads](https://img.shields.io/pypi/dm/bitccl?style=flat-square)

---

BitCCL is a [BitcartCC](https://bitcartcc.com) scripting language used for automating checkout flow and more.

It is currently in alpha stage, being separated from the [main BitcartCC repository](https://github.com/MrNaif2018/bitcart).

## Architechture

BitCCL is basically Python, but:
- Safe, with disabled import system
- Robust, with many built-in functions
- Optimized for running in BitcartCC environment

Language file extension is `.bitccl`.

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


## Built-in events 

In progress of adding

## Contributing

You can contribute to BitCCL language by suggesting new built-in functions and events to be added, as well as any ideas for improving it.
Open an [issue](https://github.com/MrNaif2018/bitccl/issues/new/choose) to suggest new features
