#!/usr/bin/env python3
"""Safely get value"""


from typing import TypeVar, Dict, Any, Optional

K = TypeVar('K')
V = TypeVar('V')


def safely_get_value(dct: Dict[K, V], key: K, default: Optional[V] = None) -> V:
    """
    Safely get the value associated with the key from the dictionary.

    Parameters:
    - dct (Dict[K, V]): A dictionary with keys of type K and values of type V.
    - key (K): The key to look up in the dictionary.
    - default (Optional[V]): The default value to return if the key is not
    found (default is None).

    Returns:
    - V: The value associated with the key, or the default value if the key
    is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
