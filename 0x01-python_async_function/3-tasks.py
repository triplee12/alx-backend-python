#!/usr/bin/env python3
"""Asyncio task."""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Asyncio task.

    Args:
        max_delay(int): maximum number of await time
    Returns:
        Task
    """
    loop = asyncio.get_event_loop()
    task: asyncio.Task = loop.create_task(wait_random(max_delay))
    return task
