#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from operator import itemgetter

L1 = [36, 5, -12, 9, -21]
print(sorted(L1))
print(sorted(L1, key=abs))
print(sorted(L1, key=abs, reverse=True))

L2 = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(L2))
print(sorted(L2, key=str.lower))
print(sorted(L2, key=str.lower, reverse=True))

#   itemgetter(): 获取字典键、值或多远列表指定维的数据
L3 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L3))
print(sorted(L3, key=itemgetter(1)))
print(sorted(L3, key=itemgetter(1), reverse=True))


x = [
    {"语文": 80, "数学": 90, "英语": 70, "物理": 92, "化学": 83},
    {"语文": 82, "数学": 70, "英语": 78, "物理": 90, "化学": 80},
    {"语文": 86, "数学": 89, "英语": 73, "物理": 67, "化学": 88},
    {"语文": 76, "数学": 86, "英语": 60, "物理": 82, "化学": 79}
]

print(sorted(x, key=lambda x: x["物理"]))
print(sorted(x, key=itemgetter('语文')))
