#!/usr/bin/env python3
import os
import sys

from bitccl import run


def main():
    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} file.bccl")

    filename = sys.argv[1]
    if not os.path.exists(filename):
        sys.exit(f"File {filename} does not exist")
    try:
        with open(filename) as f:
            source = f.read()
    except OSError:
        sys.exit("Error reading input file")

    error_message = run(source, filename)
    if error_message:
        print(error_message, end="")
