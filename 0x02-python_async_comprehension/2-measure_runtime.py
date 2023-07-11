#!/usr/bin/env python3
"""Run time for four parallel comprehensions."""

import asyncio
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the runtime.

    Returns:
        float: the runtime time.
    """
    start_time: float = perf_counter()

    # Execute async_comprehension four times in parallel
    await asyncio.gather(*[async_comprehension() for _ in range(4)])

    end_time: float = perf_counter()
    runtime: float = end_time - start_time
    return runtime
