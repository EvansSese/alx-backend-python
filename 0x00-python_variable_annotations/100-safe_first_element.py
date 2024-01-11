#!/usr/bin/env python3
"""Function to return first item of list"""


from typing import List, Optional, TypeVar


T = TypeVar('T')


def safe_first_element(lst: List[T]) -> Optional[T]:
    """
    Get the first element of the list safely.

    Parameters:
    - lst (List[T]): A list of elements of any type.

    Returns:
    - Optional[T]: The first element of the list, or None if the list is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
