#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test script of __getitem__"""
__author__ = 'Jason Yang'


class Fib(object):
    def __getitem__(self, i):
        if isinstance(i, int):
            a, b = 1, 1
            for n in range(i):
                a, b = b, a+ b
            return a
        if isinstance(i, slice):
            start = i.start
            stop = i.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a+b
            return L


for n in Fib():
    if n < 6800:
        print(n)
    else:
        break

print(Fib()[0])
print(Fib()[5])
print(Fib()[100])
print(Fib()[0:5])
print(Fib()[:10])
