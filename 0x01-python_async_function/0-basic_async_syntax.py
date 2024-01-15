#!/usr/bin/env python3
"""An asynchronous coroutine"""

import asyncio
import random


async def wait_random(max_delay=10):
    """Async wait_random function/coroutine"""
    await asyncio.sleep(random.uniform(0, max_delay))


if __name__ == "__main__":
    wait_random()
