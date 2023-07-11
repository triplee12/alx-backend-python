#!/usr/bin/env python3
"""Async Generator."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    """
    Async Generator.

    Yields:
        Generator: yield random number after waiting for 1 second
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
