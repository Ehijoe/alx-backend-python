#!/usr/bin/env python3
"""Coroutine to generate numbers."""
from random import uniform
from asyncio import sleep
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yield 10 random numbers asynchronously."""
    for i in range(10):
        await sleep(1.0)
        yield uniform(0, 10)
