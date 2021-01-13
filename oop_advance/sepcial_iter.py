#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test script of __iter__"""
__author__ = 'Jason Yang'


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        #   if self.a > 1000:
        #       raise StopIteration()
        return self.a


for n in Fib():
    if n < 1000:
        print(n)
    else:
        break
