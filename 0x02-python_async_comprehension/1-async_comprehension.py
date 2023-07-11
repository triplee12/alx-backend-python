#!/usr/bin/env python3
"""Async comprehension."""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Async comprehension.

    Returns:
        List[float]: list of floats
    """
    lst = [i async for i in async_generator()]
    return lst
