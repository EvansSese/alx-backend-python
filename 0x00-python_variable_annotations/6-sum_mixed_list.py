#!/usr/bin/env python3
"""Function to add list items"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Function to add list items"""
    return sum(mxd_list)


if __name__ == "__main__":
    sum_mixed_list([0.0, 0])
