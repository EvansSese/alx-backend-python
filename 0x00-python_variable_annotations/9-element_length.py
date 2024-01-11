#!/usr/bin/env python3
"""Annotating a function"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotating a function"""
    return [(i, len(i)) for i in lst]


if __name__ == "__main__":
    element_length(['a'])
