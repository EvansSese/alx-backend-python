#!/usr/bin/env python3
"""Function to add list items"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Function to add list items"""
    return sum(input_list)


if __name__ == "__main__":
    sum_list([0.0, 0.0])
