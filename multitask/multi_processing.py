#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test script of multiprocessing"""
__author__ = 'Jason Yang'

import os
from multiprocessing import Process


def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test', ))
    print('Start child process.')
    p.start()
    p.join()
    print('End child process.')
