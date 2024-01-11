#!/usr/bin/env python3
"""Annotating a function"""


from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    return [(i, len(i)) for i in lst]


if __name__ == "__main__":
    element_length(['a'])
