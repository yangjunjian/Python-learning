#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""a test script of error re-raise"""
__author__ = 'Jason Yang'


def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n


def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise


bar()
print('END')
