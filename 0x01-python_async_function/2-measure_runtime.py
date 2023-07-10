#!/usr/bin/env python3
"""Measure the runtime."""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure wait time.

    Args:
        n (int): number of time
        max_delay(int): maximum number of await time
    Returns:
    float: total time divided by n
    """
    start_time: float = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(wait_n(n, max_delay))
    loop.close()
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
