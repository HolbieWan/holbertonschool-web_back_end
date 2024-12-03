#!/usr/bin/env python3
"""Module with a function that sums-up a list of mixed values"""

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """function sum_mixed_list which takes a list mxd_lst of integers
    and floats and returns their sum as a float"""
    return float(sum(mxd_lst))
