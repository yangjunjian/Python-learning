#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test script of json"""
__author__ = 'Jason Yang'

import json
import os

d = dict(name='Bob', age=20, score=88)
fp = os.path.join(os.path.abspath('.'), 'test.json')

#   使用json序列化
d2s = json.dumps(d)
print(d2s, type(d2s))

#   使用json反序列化
s2d = json.loads(d2s)
print(s2d, type(s2d))

#   使用json序列化并保存到file-like object
with open(fp, 'w') as f:
    json.dump(d, f)

#   使用json从file-like object反序列化
with open(fp, 'r') as f:
    f2d = json.load(f)
    print(f2d, type(f2d))


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student object (%s, %s, %s)' % (self.name, self.age, self.score)

    __repr__ = __str__


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


def dict2student(dt):
    return Student(dt['name'], dt['age'], dt['score'])


s = Student('Bob', 20, 98)
#   std_data = json.dumps(s, default=student2dict)
std_data = json.dumps(s, default=lambda obj: obj.__dict__)
print('Dump student:', std_data)

#   rebuild = json.loads(std_data, object_hook=dict2student)
rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
print(rebuild)
