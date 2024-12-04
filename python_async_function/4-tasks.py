#!/usr/bin/env python3
"""Module with a function wait_n that returns a list of all delays"""

import asyncio
from typing import List
bubble_sort = __import__('bubble_sort').bubble_sort
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Function that takes in 2 int arguments (n and max_delay)
    spawns wait_random n times with max_delay
    and returns the list of all the delays (float values)"""
    i = 0
    delays_list = []
    while (i < n):
        result = task_wait_random(max_delay)
        delays_list.append(result)
        i += 1
    result_list = await asyncio.gather(*delays_list)
    bubble_sort(result_list)
    return result_list

# better way:
    # task = [task_wait_random(max_delay) for _ in range(n)]
    # delays = await asyncio.gather(*task)
