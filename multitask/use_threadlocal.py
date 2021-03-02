#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test script of ThreadLocal"""
__author__ = 'Jason Yang'

import threading

#   创建全局ThreadLocal对象
local_school = threading.local()


def greeting_student():
    #   获取当前线程关联的student
    std = local_school.student
    print('Hello, %s (in %s)!' % (std, threading.current_thread().name))


def process_thread(name):
    #   绑定ThreadLocal的student：
    local_school.student = name
    greeting_student()


t1 = threading.Thread(target=process_thread, args=('Alice', ), name='Thread A')
t2 = threading.Thread(target=process_thread, args=('Bob', ), name='Thread B')
t1.start()
t2.start()
t1.join()
t2.join()
