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
    random_list = [asyncio.create_task(wait_random(max_dealy))
                   for x in range(n)]

    completed_tasks = []
    for task in asyncio.as_completed(random_list):
        completed_tasks.append(await task)

    return completed_tasks
