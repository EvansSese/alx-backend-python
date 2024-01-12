#!/usr/bin/env python3
"""Safely get value"""


from typing import TypeVar, Mapping, Any, Union, Optional
T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any,
                     default: Optional[T] = None) -> Union[T, None]:
    """
    Safely get the value associated with the key from the dictionary.

    Parameters:
    - dct (Mapping[Any, T]): A mapping (e.g., dictionary) with keys of
    any type and values of type T.
    - key (Any): The key to look up in the dictionary.
    - default (Optional[T]): The default value to return if the key
    is not found (default is None).

    Returns:
    - Union[T, None]: The value associated with the key, or the default
    value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
