#!/usr/bin/env python3
"""Pagination"""

import csv
import math
from typing import List


def index_range(page: int, page_size: int):
    """Helper function that return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes to return in a list
    for those particular pagination parameters."""
    a = (page - 1) * page_size
    b = page * page_size
    return (a, b)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Method that takes two integer arguments: page with default
        value 1 and page_size with default value 10 and returns the appropriate
        page of the dataset (list)."""

        assert isinstance(
            page, int) and page > 0, "Page must be positiv integer"
        assert isinstance(
            page_size, int) and page_size > 0, "Page_size must be positiv \
                integer"

        data_list = self.dataset()
        start_index, end_index = index_range(page, page_size)

        if start_index < len(data_list):
            return data_list[start_index:end_index]
        else:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Method that takes two integer arguments: page with default
        value 1 and page_size with default value 10 and returns the appropriate
        page of the dataset (dictionnary)."""
        assert isinstance(
            page, int) and page > 0, "Page must be positiv integer"
        assert isinstance(
            page_size, int) and page_size > 0, "Page_size must be positiv \
                  integer"

        data_list = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page + 1 < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": page_size,
            "page": page,
            "data": data_list,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
