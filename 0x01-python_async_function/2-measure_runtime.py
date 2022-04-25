#!/usr/bin/env python3
""" Multiple coroutines """

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ return total_time / n """
    t1_start = time.time()
    asyncio.run(wait_n(n, max_delay))
    t1_end = time.time()
    total_time = t1_end - t1_start
    return total_time / n
