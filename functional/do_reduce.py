#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

#   利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    index = 0
    if '.' in s:
        idx = s.index('.')
        index = len(s) - idx - 1
        s = s[:idx]+s[idx+1:]
    dict ={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
    
    def prod(x,y):
        return 10*x+y
    
    def c2i(c):
        return dict[c]
    return reduce(prod,map(c2i,s))/pow(10,index)

#   方法二：先获取到每个字符对应的数字，以及'.'的位置；在'.'之前的通过10*x+y累计，在'.'之后的通过x+y/pow(10,n)累计
CHAR_TO_FLOAT = {
    '0':0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}


def str2float(s):
    #   将字符串转换为一串数字map，小数点用-1表示
    nums = map(lambda c: CHAR_TO_FLOAT[c], s)
    point = 0

    def to_float(f, n):
        nonlocal point
        #   判断是小数点前还是小数点后的数字
        if n == -1:
            point = 1
            return f
        #   分别对小数点前和小数点后的数字进行乘或除计算
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point

    return reduce(to_float, nums, 0.0)


print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))
