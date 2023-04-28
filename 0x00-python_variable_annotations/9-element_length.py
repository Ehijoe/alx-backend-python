#!/usr/bin/python3
"""Duck typing."""
from typing import Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> list[tuple[Sequence, int]]:
    """Return the lengths of the elements of a list."""
    return [(i, len(i)) for i in lst]
