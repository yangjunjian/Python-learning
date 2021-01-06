#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test script of class/instance"""
__author__ = 'Jason Yang'


class Student(object):
    __slots__ = ('name', 'age')


class GraduateStudent(Student):
    pass


s = Student()
s.name = 'Jason'
s.age = 25

try:
    s.score = 99
except AttributeError as e:
    print('AttributeError:', e)

g = GraduateStudent()
g.score = 100
print('g.score =', g.score)
