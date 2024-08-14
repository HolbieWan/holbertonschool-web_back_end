#!/usr/bin/env python3
"""Annotate the below function’s parameters and
 return values with the appropriate types"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list of floats and integers"""
    return float(sum(mxd_lst))
