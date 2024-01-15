#!/usr/bin/env python3
"""Measure runtime of async function"""

from time import time
from asyncio import run


def measure_time(n: int, max_delay: int) -> float:
    wait_n = __import__('1-concurrent_coroutines').wait_n
    start = time()
    run(wait_n(n, max_delay))
    end = time()
    runtime = (end - start) / n
    return runtime


if __name__ == "__main__":
    measure_time(0, 0)
