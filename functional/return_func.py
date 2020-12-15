#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def sum(*args):
    ax = 0
    for i in args:
        ax = ax + i
    return ax


print(sum(1, 2, 3, 4, 5))


def lazy_sum(*args):
    def f():
        ax = 0
        for i in args:
            ax = ax + i
        return ax
    return f


print(lazy_sum(1, 2, 3, 4, 5))
print(lazy_sum(1, 2, 3, 4, 5)())
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)
print(f1() == f2())


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        #   返回为函数时，不会立即执行，需要在调用函数时才会执行；如需立即执行可使用fs.append(f())
        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1, f2, f3)
print(f1(), f2(), f3())


def count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


f1, f2, f3 = count()
print(f1, f2, f3)
print(f1(), f2(), f3())
