import sys

from .cli import cli, get_args_from_cli
from .model import continuous_review


def main():
    args = get_args_from_cli(cli)
    k, q, r = continuous_review(args)
    print(f"Value of K*: {k}")
    print(f"Value of Q*: {q}")
    print(f"Value of r*: {r}")
    return k, q, r
