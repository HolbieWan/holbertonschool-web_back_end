#!/usr/bin/env python3
"""Module with function measure_time()
that measures the total execution time for wait_n() coroutine"""

import time
import asyncio
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """function measure_time()
    that measures the total execution time for wait_n() coroutine
    and returns total_time / n"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
