#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test script of property"""
__author__ = 'Jason Yang'


class Student(object):
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('Score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('Score must between 0 ~ 100!')
        self.__score = value


jason = Student()
jason.score = 99
print('jason.score = %s' % jason.score)
jason.score = 'a'
