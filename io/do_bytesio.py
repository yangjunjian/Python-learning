#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""a test script of StringIO"""
__author__ = 'Jason Yang'

from io import BytesIO

#   write to BytesIO:
f = BytesIO()
f.write(b'hello')
f.write(b' ')
f.write(b'world!')
#   getvalue(): b'hello world!'
print('getvalue():', f.getvalue())

#   read from BytesIO
f = BytesIO('临江仙 宋·苏轼\n'
            '夜饮东坡醒复醉，\n归来仿佛三更。\n家童鼻息已雷鸣。\n敲门都不应，\n倚杖听江声。\n\n'
            '长恨此身非我有，\n何时忘却营营。\n夜阑风静縠纹平。\n小舟从此逝，\n江海寄余生。'.encode('utf-8'))
while True:
    s = f.readline()
    if s == b'':
        break
    print(s)
