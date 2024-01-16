#!/usr/bin/env python3
"""Async comprehension"""

import asyncio
import random
from typing import List


async def async_comprehension() -> List[float]:
    """Async comprehension"""
    async_generator = __import__('0-async_generator').async_generator
    return [i async for i in async_generator()]
