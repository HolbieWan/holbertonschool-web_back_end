#!/usr/bin/env python3
"""Module with basic async function"""

import asyncio
import random


async def wait_random(max_delay: int=10) -> int:
    """asynchronous coroutine that takes in an integer argument
    that waits for a random delay between 0 and max_delay seconds
    and eventually returns it."""
    await asyncio.sleep(random.uniform(0, max_delay))
    return max_delay
