#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""a test script of StringIO"""
__author__ = 'Jason Yang'

from io import StringIO

#   write to StringIO:
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
#   getvalue(): 'hello world!'
print('getvalue():', f.getvalue())
#   当前指针已在最后，read()读取不到内容；write()同（从当前指针位置开始写入）
print('read():', f.read())

#   read from StringIO:
f = StringIO('临江仙 宋·苏轼\n'
             '夜饮东坡醒复醉，\n归来仿佛三更。\n家童鼻息已雷鸣。\n敲门都不应，\n倚杖听江声。\n\n'
             '长恨此身非我有，\n何时忘却营营。\n夜阑风静縠纹平。\n小舟从此逝，\n江海寄余生。')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
