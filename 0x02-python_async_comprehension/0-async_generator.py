#!/usr/bin/env python3
'''
A coroutine  async_generator10 that loops 10 times,
each time asynchronously wait 1 second, then yield a random number
between 0 and 10. Use the random module.
'''


import random
from typing import Generator
import asyncio


async def async_generator() -> Generator[float, None, None]:
    ' loops 10 times'
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
