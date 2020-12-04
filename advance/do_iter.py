#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

from collections.abc import Iterable, Iterator 

#生成器：generator
def g():
    yield 1
    yield 2
    yield 3

'''
集合数据类型如list, tuple, dict, set, str, generator等
可以直接作用于for循环的对象统称为可迭代对象：Iterable。
'''
print('Iterable? [1,2,3]:',isinstance([1,2,3],Iterable))
print('Iterable? (1,2,3):',isinstance((1,2,3),Iterable))
print('Iterable? \'abc\':',isinstance('abc',Iterable))
print('Iterable? 123:',isinstance(123,Iterable))
print('Iterable? g():',isinstance(g(),Iterable))

#字典的迭代
d = {'a': 1, 'b': 2, 'c': 3}
print(d.keys())
print(d.values())
print(d.items())

for k,v in d.items():
    print(k,v)

'''
迭代器：Iterator。可以被next()函数调用并不断返回下一个返回值的对象称为迭代器。
可以使用iter()函数把list, dict, str等Iterable的对象变成Iterator。
'''

it = iter([1, 2, 3, 4, 5])
for x in it:
    print(x)

#通过next()函数实现for效果
it = iter([1, 2, 3, 4, 5])
while True:
    try:
        next(it)
    except StopIteration:
        break
