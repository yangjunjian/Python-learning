#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def is_odd(n):
    if n % 2 == 1:
        return True

print(list(filter(is_odd,range(100))))


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


#   筛选回文数


def natural_nums():
    #   构建一个自然数生成器
    n = 1
    while True:
        yield n
        n = n + 1


def is_reversible(n):
    #   判断是否回文数：通过转换为列表
    n_to_l = list(str(n))
    n_to_l.reverse()
    n_reversed = int(''.join(n_to_l))
    if n == n_reversed: #   n == int(str(n)[::-1]) 通过字符串的切片功能进行逆序排列
        return True


def palindrome_nums():
    nn = natural_nums()
    while True:
        n = next(nn)
        nn = filter(is_reversible, nn)
        yield n


for n in palindrome_nums():
    if n < 1000:
        print(n)
    else:
        break
