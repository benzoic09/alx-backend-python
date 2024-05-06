#!/usr/bin/env python3
""" that takes in 2 int arguments (in this order):
n and max_delay"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """takes 2 args"""
    task = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*task)
    return sorted(results)
