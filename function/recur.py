#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# 利用递归函数计算阶乘
# N! = 1 * 2 * 3 * ... * N
def fact(n):
    i = 1
    if n == 1:
        return 1
    return n*fact(n-1)

#使用尾递归方式
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
    

#汉诺塔 - a,b,c代表三根柱子，n代表a柱子的环数目，借助柱子b将所有环转移到柱子c(从上到下环依次增大，大环不能在小环上面)。
#数学逻辑：分解：第一步，将除最下面环以外的环转移到中专柱，此为函数f(n-1)，第二步将最后的环放到目标柱，第三步将中转柱的(n-1)个环转移到目标柱。
def move(n,a,b,c):
  if n == 1:
    print (a,'-->',c)
    return
  else:
    move(n-1,a,c,b)
    print (a,'-->',c)
    move(n-1,b,a,c)
    return
    
#使用递归函数生成Fibonacci数列（会导致栈溢出）
def fb(n):
  if n in (1,2):
    return 1
  else:
    return fb(n-1)+fb(n-2)
