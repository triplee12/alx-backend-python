#!/usr/bin/env python3
"""Complex types - list of floats."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of the list of floats.

    Args:
        input_list (floar): list of floats

    Returns:
        float: sum of the list of floats
    """
    total = 0
    for i in input_list:
        total += i
    return total
