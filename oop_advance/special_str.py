#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test script of __str__, __repr__"""
__author__ = 'Jason Yang'


class Student(object):
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return 'Student object: (name: %s)' % self.__name
    
    __repr__ = __str__


print(Student('Jason'))
