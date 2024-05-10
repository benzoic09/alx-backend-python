#!/usr/bin/env python3
"""task 4"""
import asyncio
from typing import List
from random import uniform
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Coroutine that waits for n random delays using asyncio.Tasks."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
