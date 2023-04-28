#!/usr/bin/python3
"""TypeVar."""
from typing import TypeVar, Union, Any, Mapping

T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Safely get a value from a dictionary."""
    if key in dct:
        return dct[key]
    else:
        return default
