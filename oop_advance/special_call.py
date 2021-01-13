#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test script of __call__"""
__author__ = 'Jason Yang'


class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


s= Student('Jason')
s()


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __call__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


s = Chain()
print(s.status.user.timeline.list)
print(s.users('michael').repos)
