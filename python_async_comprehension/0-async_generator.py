#!/usr/bin/env python3
'''Module with coroutine: async_generator'''

from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[int, None, None]:
    """ coroutine will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10"""
    for i in range(10):
        i = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield(i)
