#!/usr/bin/env python3
""" simple inplementation of pagination"""

import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple:
    """ return a tuple of size two
    containing a start index and an end index """
    return (page - 1) * page_size, page * page_size


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
        """ return with the page with index"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        index = index_range(page, page_size)
        return self.dataset()[index[0]:index[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """return a dictionary"""
        data = self.get_page(page, page_size)
        total_items = math.floor(len(self.dataset()) / page_size)
        next_page = page + 1 if total_items > page else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': page_size, 'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_items
        }
