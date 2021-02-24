#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test script of threading"""
__author__ = 'Jason Yang'

import time
import threading


#   新线程执行的代码
def loop():
    print('Thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('Thread %s >>> %s' % (threading.current_thread().name, n))
    print('Thread %s ended.' % threading.current_thread().name)


print('Thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('Thread %s ended.' % threading.current_thread().name)
