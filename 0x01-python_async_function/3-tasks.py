#!/usr/bin/env python3
"""Async tasks"""

import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates an async task"""
    task = asyncio.create_task(wait_random(max_delay))
    return task


if __name__ == "__main__":
    task_wait_random(0)
