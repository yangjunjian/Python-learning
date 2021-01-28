#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""a test script of logging"""
__author__ = 'Jason Yang'
import logging
logging.basicConfig(level=logging.INFO)


def foo(s):
    n = int(s)
    logging.info('n = %s' % n)
    return 10 / n


def main():
    foo('0')


main()
