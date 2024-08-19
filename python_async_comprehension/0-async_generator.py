#!/usr/bin/env python3
"""Async Generator"""

import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """Async generator function that yelds a random number between 0 an 10"""
    for i in range(10):
        i = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield (i)
