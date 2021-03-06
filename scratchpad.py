# from typing import List
#
# lst = [0, 1, 2, 3]
#
#
# def sm(fst: int, sec: int, thd: int, fth: int):
#     print(fst + sec + thd + fth)
#
#
# sm(*lst)
#
#
# def generator2():
#     for i in range(10):
#         print(i)
#         yield i
#
#
# def generator3():
#     for j in range(10, 20):
#         print(j)
#         yield j
#
#
# def generator():
#     yield from generator2()
#     yield from generator3()
#
#
# d = generator()
#
# next(d)
# next(d)
# next(d)
# next(d)
#
# d = map(int, [1, 2, 3])
# type(d)
# print(next(d))
# print(next(d))
# print(next(d))
#
# from itertools import cycle
#
#
# def endless():
#     yield from cycle((9, 8, 7, 6))
#
#
# e = endless()
# total = 0
# for i in e:
#     if total < 30:
#         print(i, ' ')
#         total += i
#     else:
#         print()
#         break
#
# print(next(e))
# print(next(e))
# print(next(e))

import asyncio


async def mygen(u: int = 10):
    """Yield powers of 2."""
    i = 0
    while i < u:
        yield 2 ** i
        i += 1
        await asyncio.sleep(0.1)


async def main():
    # This does *not* introduce concurrent execution
    # It is meant to show syntax only
    g = [i async for i in mygen()]
    f = [j async for j in mygen() if not (j // 3 % 5)]
    return g, f


g, f = asyncio.run(main())
g
f


async def main_test():
    print('Hello')
    await asyncio.sleep(5)
    print('David')


test = main_test()

type(test)


# not concurrently run in event loop
async def example(message):
    print("start of example():", message)
    await asyncio.sleep(1)
    print("end of example():", message)


async def main():
    # Start coroutine twice (hopefully they start!)
    first_awaitable = example("First call")
    second_awaitable = example("Second call")
    # Wait for coroutines to finish
    await first_awaitable
    await second_awaitable


asyncio.run(main())

import time


# concurrently run in event loop
async def example(message, delay):
    print("start of example():", message)
    await asyncio.sleep(delay)
    # return('done calling ', message)
    print("end of example():", message)


async def main():
    # Start coroutine twice (hopefully they start!)
    print(f"started at {time.strftime('%X')}")
    first_awaitable = await example("First call", 5)
    second_awaitable = await example("Second call", 1)
    # Wait for coroutines to finish
    print(first_awaitable)
    print(second_awaitable)
    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())


async def print_after(message, delay):
    """Print a message after the specified delay (in seconds)"""
    print("start of example():", message)
    await asyncio.sleep(delay)
    print("end of example():", message)


async def main():
    # Start coroutine twice (hopefully they start!)
    print(f"started at {time.strftime('%X')}")
    asyncio.create_task(print_after("world!", 5))
    asyncio.create_task(print_after("Hello", 1))
    # Wait for coroutines to finish
    # await first_awaitable
    # await second_awaitable
    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())


async def print_after(message, delay):
    """Print a message after the specified delay (in seconds)"""
    print("start of example():", message)
    await asyncio.sleep(delay)
    print("end of example():", message)


async def main():
    # Start coroutine twice (hopefully they start!)
    print(f"started at {time.strftime('%X')}")
    await asyncio.gather(print_after("world!", 5),
                         print_after("Hello", 1)
                         )
    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())


async def display_date():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)

asyncio.run(display_date())