#!/usr/bin/env python3
"""Complex types - string and int/float to tuple."""
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """Return a string and a number squared."""
    return (k, float(v) ** 2)
