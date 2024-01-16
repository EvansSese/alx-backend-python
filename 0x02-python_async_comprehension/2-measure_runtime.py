#!/usr/bin/env python3
"""Measure the runtime for async comprehension"""
import asyncio
from time import time


async def measure_runtime() -> float:
    async_comprehension = (__import__('1-async_comprehension')
                           .async_comprehension)
    start = time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end = time()
    return end - start
