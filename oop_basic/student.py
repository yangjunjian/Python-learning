#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""This is a test script of class"""
__author__ = 'Jason Yang'


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def _get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 75:
            return 'B'
        elif self.score >= 60:
            return 'C'
        else:
            return 'D'

    def print_score(self):
        print('%s: %s - %s' % (self.name, self.score, self._get_grade()))


jason = Student('Jason', 90)
jason.print_score()
