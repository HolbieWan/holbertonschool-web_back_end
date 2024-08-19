#!/usr/bin/env python3
"""Async Comprehension"""

import asyncio
import random
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total execution time for running async_comprehension
    four times in parallel and returns the total time for execution.
    """
    start_time = time.time()

    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())

    end_time = time.time()
    total_time = end_time - start_time

    return total_time
