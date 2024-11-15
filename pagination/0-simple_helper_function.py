#!/usr/bin/env python3
"""Pagination"""


def index_range(page: int, page_size: int):
    """Helper function that return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes to return in a list
    for those particular pagination parameters."""
    a = (page - 1) * page_size
    b = page * page_size
    return (a, b)
