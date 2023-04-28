#!/usr/bin/env python3
"""Duck typing."""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return the lengths of the elements of a list."""
    return [(i, len(i)) for i in lst]
