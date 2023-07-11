#!/usr/bin/env python3
''' asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random
that waits for a random delay between 0 and max_delay
(included and float value) seconds and eventually returns it.
'''


import random as rd
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    'waits for a random delay'
    waitTime = max_delay * rd.random()
    await asyncio.sleep(waitTime)
    return waitTime
