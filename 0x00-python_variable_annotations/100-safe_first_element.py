#!/usr/bin/env python3
"""Using the Any type."""
from typing import Any, Sequence, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of a list."""
    if lst:
        return lst[0]
    else:
        return None
