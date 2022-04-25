ASYNC

#!/usr/bin/env python3
"""
asynchronous coroutine
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_dealy: int) -> List[float]:
    """
    Import wait_random from the previous python file that
    you’ve written and write an async routine called wait_n
    that takes in 2 int arguments (in this order): n and max_delay.
    You will spawn wait_random n times with the specified max_delay.
    """
    random_list = []
    for _ in range(n):
        random_list.append(asyncio.create_task(wait_random(max_dealy)))

    task_list_ascompleted = []
    for t in asyncio.as_completed(random_list):
        task_list_ascompleted.append(await t)

    return task_list_ascompleted
