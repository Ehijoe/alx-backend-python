#!/usr/bin/env python3
"""Coroutine to generate numbers."""
from random import uniform
from time import sleep


async def async_generator():
    """Yield 10 random numbers asynchronously."""
    async for i in range(10):
        sleep(1)
        yield uniform(0, 10)
