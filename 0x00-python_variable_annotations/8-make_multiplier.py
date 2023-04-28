#!/usr/bin/python3
"""Function annotation."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies by a float."""
    def f(n):
        """Multiply n by a multiplier."""
        return n * multiplier
    return f
