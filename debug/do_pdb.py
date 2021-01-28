#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""a test script of pdb"""
__author__ = 'Jason Yang'
import pdb


def foo(s):
    n = int(s)
    pdb.set_trace()
    return 10 / n


def main():
    foo('0')


main()
