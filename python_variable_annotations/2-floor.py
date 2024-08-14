#!/usr/bin/env python3
"""Type-annotated function floor that takes a float n
 as argument and returns the floor of the float"""


def floor(n: float) -> int:
    """Return the floor of a float"""
    return int(n) if n >= 0 else int(n) - (n % 1 != 0)
