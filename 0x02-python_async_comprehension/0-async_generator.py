#!/usr/bin/env python3
"""Coroutine to generate numbers."""
from random import uniform
from asyncio import sleep
from typing import Iterator


async def async_generator() -> Iterator[float]:
    """Yield 10 random numbers asynchronously."""
    for i in range(10):
        yield uniform(0, 10)
        await sleep(1.0)
