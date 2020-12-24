#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""This is a test script of class"""
__author__ = 'Jason Yang'


# 要让class内部属性和方法不被外部访问，可在属性和方法名称前加两个下划线，将其变为私有变量


class Student(object):
    def __init__(self, name, score, gender):
        self.__name = name
        self.__score = score
        self.__gender = gender

    def __get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 75:
            return 'B'
        elif self.__score >= 60:
            return 'C'
        else:
            return 'D'

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('invalid score')

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender.lower() in ('male', 'female'):
            self.__gender = gender
        else:
            raise ValueError('invalid gender')

    def print_score(self):
        print('%s: %s - %s' % (self.__name, self.__score, self.__get_grade()))


jason = Student('Jason', 90, 'Male')
print(jason.get_name())
print(jason.get_score())
print(jason.get_gender())
jason.set_gender('Female')
jason.set_score(87)
print(jason.get_score())
print(jason.get_gender())
