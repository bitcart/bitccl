# Release Notes

## Latest changes

## 0.4.3

Don't install a separate tests package, but include tests in source tarball

## 0.4.2

Rename BitcartCC to Bitcart

## 0.4.1

Fix PyPI readme

## 0.4.0

Change license to MIT license

## 0.3.1

Python 3.11 support

## 0.3.0

We now support Python 3.8+ only

## 0.2.0

Properly use event loop
We now support using `asyncio.run` without crashes

## 0.1.1

Python 3.10 support

## 0.1.0

Better, safer compiler by using RestrictedPython

Now it should not be possible to get access to arbitrary modules via existing python objects available.

For more details see [How does BitCCL secure the users](https://github.com/bitcart/bitccl/blob/master/README.md#how-does-bitccl-secure-the-users)

## 0.0.6

Drop python 3.6 support (we support 3 latest python releases)

## 0.0.5

License change to LGPLv3+

Python 3.9 support

Fixes for SDK 1.0

Full library reformatting and dependencies upgrade

## 0.0.4

Version 0.0.4
Integrated HTTP Client and SDK, plugins system and new events.

## 0.0.3

Add ability to pass custom config, cleanup event listeners on finalization
run function now accepts optional parameter config (dict), which should contain necessary config keys for script execution. Otherwise local config is used.

## 0.0.2

Fixed event dispatching, imports isolation, added tests, fixed PyPi logo

## 0.0.1

Initial release
