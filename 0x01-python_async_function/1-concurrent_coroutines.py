#!/usr/bin/env python3
"""
asynchronous coroutine
"""


from typing import List
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_dealy: int) -> List[float]:
    """
    Import wait_random from the previous python file that
    you’ve written and write an async routine called wait_n
    that takes in 2 int arguments (in this order): n and max_delay.
    You will spawn wait_random n times with the specified max_delay.
    """
    """
    random_list: List[float] = []
    for x in range(n):
        task1 = asyncio.create_task(wait_random(max_dealy))
        random_list.append(await task1)
    """
    return await asyncio.gather(*[wait_random(max_dealy) for x in range(n)])
