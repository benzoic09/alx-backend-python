#!/usr/bin/env python3
"""Task zero"""
import asyncio
import random


async def async_generator():
    """Coroutine that yields a random number between 0 and 10 after
    asynchronously waiting for 1 second."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
