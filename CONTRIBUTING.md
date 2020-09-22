# Contributing to BitCCL

Welcome, and thank you for your interest in contributing to BitCCL!

Our [central contributing guidelines](https://github.com/bitcartcc/bitcart/blob/master/CONTRIBUTING.md) apply to all BitcartCC repositories.

Below are the instructions for setting up development environment with BitCCL.

## Setting up development environment

Some general advice can be found in our [central contributing guidelines](https://github.com/bitcartcc/bitcart/blob/master/CONTRIBUTING.md#setting-up-development-environment).

Instructions:

```bash
git clone https://github.com/<<<your-github-account>>>/bitccl.git
cd bitccl
virtualenv env
source env/bin/activate
pip3 install -e .
pip3 install -r test-requirements.txt # for tests
```

From now on, development environment is ready.

Make sure to follow [our coding guidelines](https://github.com/bitcartcc/bitcart/blob/master/CODING_STANDARDS.md) when developing.

To run all checks before commiting, use `make` command.

# Thank You!

Your contributions to open source, large or small, make great projects like this possible. Thank you for taking the time to contribute.
