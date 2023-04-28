#!/usr/bin/env python3
"""Any."""
from typing import Any, Sequence


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Any:
    """Return the first element of a list."""
    if lst:
        return lst[0]
    else:
        return None
