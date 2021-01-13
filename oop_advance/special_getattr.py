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
            return lambda: 25
        raise AttributeError('Student object has no attribute: %s' % attr)


s = Student('Jason Yang')
print(s.name)
print(s.score)
print(s.age())
print(s.grade)
