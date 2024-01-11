#!/usr/bin/env python3
""" Function that returns a function"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Function that returns a function"""
    def multiplier_func(x: float) -> float:
        return x * multiplier
    return multiplier_func


if __name__ == "__main__":
    make_multiplier(0.0)
