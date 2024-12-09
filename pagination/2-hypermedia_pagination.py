#!/usr/bin/env python3
'''Module with an helper function: index_range'''
import csv
import math
from typing import Tuple, List, Dict


def index_range(page: int, page_size: int) -> tuple:
    '''function that takes two integer arguments page and page_size
    and returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes'''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


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
        assert (isinstance(page, int) and page > 0)
        assert (isinstance(page_size, int) and page_size > 0)
        data_list = self.dataset()
        start_index, end_index = index_range(page, page_size)
        if start_index < len(data_list):
            return data_list[start_index:end_index]
        else:
            return []
        
    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict{int, int, List[List], int, int, int}:
        