#!/usr/bin/env python3
"""Module with coroutine: measure_runtime"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """coroutine that executes async_comprehension four times in parallel,
    then returns the total runtime and returns it."""
    start = time.time()
    await asyncio.gather(*[async_comprehension() for i in range(4)])
    end = time.time()
    return (end - start)
