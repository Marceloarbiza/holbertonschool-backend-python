#!/usr/bin/env python3
""" ASYNC COMPREHENSIONS """

from typing import List
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ return a list of random numbers """
    result = [i async for i in async_generator()]
    return result
