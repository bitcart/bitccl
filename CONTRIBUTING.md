# Contributing to BitCCL

Welcome, and thank you for your interest in contributing to BitCCL!

Our [central contributing guidelines](https://github.com/bitcart/bitcart/blob/master/CONTRIBUTING.md) apply to all Bitcart repositories.

Below are the instructions for setting up development environment with BitCCL.

## Setting up development environment

Some general advice can be found in our [central contributing guidelines](https://github.com/bitcart/bitcart/blob/master/CONTRIBUTING.md#setting-up-development-environment).

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

Make sure to follow [our coding guidelines](https://github.com/bitcart/bitcart/blob/master/CODING_STANDARDS.md) when developing.

This repository uses pre-commit hooks for better development experience. Install them with:

```
pre-commit install
```

It will run automatically on commits.

If you ever need to run the full pre-commit checks on all files, run:

```
pre-commit run --all-files
```

To run all checks before commiting, use `make` command.

# Thank You!

Your contributions to open source, large or small, make great projects like this possible. Thank you for taking the time to contribute.
