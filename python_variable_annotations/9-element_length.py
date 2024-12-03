#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple
"""Module with function that """


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function that take a list of iterables as argument
    and returns a list of tuples with the iterable and its lenght"""
    return [(i, len(i)) for i in lst]
