#!/usr/bin/env python3
from typing import Union
"""Module with a function that sums-up a list of mixed values"""


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    """function sum_mixed_list which takes a list mxd_lst of integers
    and floats and returns their sum as a float"""
    return float(sum(mxd_lst))
