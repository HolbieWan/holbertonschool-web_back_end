#!/usr/bin/env python3
'''Module with coroutine: async_comprehension'''
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """coroutine will collect 10 random numbers using an async comprehensing
      over async_generator, then return the 10 random numbers."""
    result = [value async for value in async_generator()]
    return result
