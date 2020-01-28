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
