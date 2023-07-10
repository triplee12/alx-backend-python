#!/usr/bin/env python3
"""Concurrent coroutines."""

import asyncio
from typing import List, Any

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Wait for n times.

    Args:
        n (int): number of time
        max_delay(int): maximum number of await time
    Returns:
    List[float]: list of delay time in float
    """
    tasks: List[Any] = [wait_random(max_delay) for _ in range(n)]
    delays: List[Any] = await asyncio.gather(*tasks)
    sorted_numbers: List[Any] = delays

    for i in range(len(sorted_numbers)):
        for j in range(i + 1, len(sorted_numbers)):
            if sorted_numbers[j] < sorted_numbers[i]:
                sorted_numbers[i] = sorted_numbers[j]
                sorted_numbers[j] = sorted_numbers[i]
    return sorted_numbers
