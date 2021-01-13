#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test script of __getattr__"""
__author__ = 'Jason Yang'


class Student(object):
    def __init__(self, name):
        self.name = name

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            #    返回函数时，变量即为调用时的参数
            return lambda x: x
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)


s = Student('Jason Yang')
print(s.name)
print(s.score)
print(s.age())
#   AttributeError: 'Student' object has no attribute 'grade'
print(s.grade)


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


s = Chain()
print(s)
print(s.status)
print(s.status.user)
print(s.status.user.timeline)
print(s.status.user.timeline.list)
