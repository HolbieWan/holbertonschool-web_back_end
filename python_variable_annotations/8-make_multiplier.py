#!/usr/bin/env python3
from typing import Callable
"""Module with a function that multiplies a float by multiplier"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    return lambda x: x * multiplier
