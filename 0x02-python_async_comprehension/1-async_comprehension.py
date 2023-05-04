#!/usr/bin/env python3
"""Using an async generator."""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return a list of numbers."""
    return [num async for num in async_generator()]
