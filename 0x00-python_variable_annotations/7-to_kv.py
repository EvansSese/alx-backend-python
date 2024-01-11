#!/usr/bin/env python3
"""Function to return tuple"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function to return tuple"""
    return k, float(v**2)


if __name__ == "__main__":
    to_kv('a', 0.0)
