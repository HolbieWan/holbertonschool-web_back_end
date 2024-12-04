#!/usr/bin/env python3
"""Module with a function wait_n that returns a list of all delays"""

import asyncio
from typing import List
bubble_sort = __import__('bubble_sort').bubble_sort
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Function that takes in 2 int arguments (n and max_delay)
    spawns wait_random n times with max_delay
    and returns the list of all the delays (float values)"""
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    bubble_sort(delays)
    return delays
