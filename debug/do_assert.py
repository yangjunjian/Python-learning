#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""a test script of assert"""
__author__ = 'Jason Yang'


def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n


def main():
    foo('0')


main()
