#!/usr/bin/env python3
"""
This function provides calculating for the start and end indices
of a given page and page size in a paginated list.
"""

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indices for a given page and page size.

    Args:
        page (int): The 1-indexed page number.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end indices.
    """

    start_index = 0
    end_index = 0

    for _ in range(page):
        start_index = end_index + 1
        end_index = start_index + page_size - 1

    return start_index, end_index
