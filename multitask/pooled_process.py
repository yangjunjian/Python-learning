#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test script of multiprocessing"""
__author__ = 'Jason Yang'

import os, time, random
from multiprocessing import Pool


def long_time_proc(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs in %.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_proc, args=(i, ))
    print('Waiting for all subprocesses done.')
    #    关闭进程池，不再接受新任务
    p.close()
    #    主进程阻塞，等待子进程退出
    p.join()
    print('All subprocesses done.')
