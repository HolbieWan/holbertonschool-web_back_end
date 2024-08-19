#!/usr/bin/env python3
"""Async Generator"""

import asyncio
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> float:
    """Async function that returns yielded numbers from async_generator()"""
    return [i async for i in async_generator()]
