#! /usr/bin/env python3
# _*_ coding:utf-8 _*_

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#复制整个列表
L1 = L[:]
print(L1)
#取前3位
print('L[0:3] =',L[0:3])
print('L[:3] =',L[:3])
#取后3位
print('L[-3:] =',L[-3:])
#每三个取一个
print('L[::3] =',L[::3])

#使用切片实现strip()函数
def trim(s):
    while True:
        if s[:1] == ' ':
            s = s[1:]
        if s[-1:] == ' ':
            s = s[:-1]
        if s == '' or s[:1] != ' ' and s[-1:] != ' ':
            break
    return s
print(trim([1,2,3]))
print(trim(''))
print(trim('    '))
print(trim('  Hello,  world! '))