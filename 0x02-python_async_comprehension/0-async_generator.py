#!/usr/bin/env python3
"""Coroutine to generate numbers."""
from random import uniform
from time import sleep
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yield 10 random numbers asynchronously."""
    for i in range(10):
        sleep(1)
        yield uniform(0, 10)
