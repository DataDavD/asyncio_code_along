from typing import List
lst = [0, 1, 2, 3]

def sm(fst: int, sec: int, thd: int, fth: int):
    print (fst + sec + thd + fth)

sm(*lst)


def generator2():
    for i in range(10):
        print(i)
        yield i


def generator3():
    for j in range(10, 20):
        print(j)
        yield j


def generator():
    yield from generator2()
    yield from generator3()

d = generator()

next(d)
next(d)
next(d)
next(d)

d = map(int, [1, 2, 3])
type(d)
print(next(d))
print(next(d))
print(next(d))