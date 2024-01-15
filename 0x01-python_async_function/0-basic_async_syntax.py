#!/usr/bin/env python3
"""An asynchronous coroutine"""

import asyncio
import random


async def wait_random(max_delay: float = 10) -> float:
    """Async wait_random function/coroutine"""
    rand_wait = random.uniform(0, max_delay)
    await asyncio.sleep(rand_wait)
    return rand_wait


if __name__ == "__main__":
    wait_random()
