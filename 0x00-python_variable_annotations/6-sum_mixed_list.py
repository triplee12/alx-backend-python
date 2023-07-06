#!/usr/bin/python3
"""Complex types - mixed list."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of the list of integers and floats.

    Args:
        mxd_lst (int, float): list of integers and floats

    Returns:
        float: the sum of the list of integers and floats
    """
    total = 0.0

    for m in mxd_lst:
        total += m
    return total
