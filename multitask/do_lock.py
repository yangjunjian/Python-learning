#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test script of threading"""
__author__ = 'Jason Yang'

import threading

balance = 0
lock = threading.Lock()


def change_it(n):
    global balance
    balance = balance + n
    balance = balance -n


def run_thread(n):
    for i in range(2000000):
        #   先获取锁
        lock.acquire()
        #   获得锁的线程一定要释放，否则其他等待锁的线程会成为死线程
        try:
            change_it(n)
        finally:
            lock.release()


t1 = threading.Thread(target=run_thread, args=(5, ))
t2 = threading.Thread(target=run_thread, args=(8, ))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
