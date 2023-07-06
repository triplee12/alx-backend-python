#!/usr/bin/env python3
"""Complex types - string and int/float to tuple."""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Complex types - string and int/float to tuple.

    Args:
        k (str): name of the kv to convert
        v (int | float): integer or float to square

    Returns:
        Tuple[str, int]: string and int/float
    """
    return (k, v*v)
