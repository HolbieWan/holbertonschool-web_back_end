#!/usr/bin/env python3
"""Annotate the below function’s parameters and return
values with the appropriate types"""


from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function that takes a list of any  iterable wich are sequences,
    and returns a list of tuples, each containing a Sequence and
    an integer showing the lenght of the sequence"""
    return [(i, len(i)) for i in lst]
