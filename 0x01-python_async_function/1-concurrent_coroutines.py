#!/usr/bin/env python3
"""
asynchronous coroutine
"""


from typing import List
import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_dealy: int) -> List[float]:
    random_list: List[float] = []
    for x in range(n):
        task1 = asyncio.create_task(wait_random(max_dealy))
        random_list.append(await task1)

    return random_list
