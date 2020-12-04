#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

s = (x * x for x in range(5))
print(s)
for x in s:
    print(x)


#杨辉三角的完美解法：
def triangles():
    L = [1]         #定义第一行
    while True:
        yield L     #返回当前行
        L.append(0) #在行末加0，在计算下一行时，通过加末尾的0，使首位两个数字保持不变
        L = [L[i - 1] + L[i] for i in range(len(L))]

#Fibonacci数列生成的几中方式
#使用生成器生成Fibonacci数列
def fib():
    a,b = 0,1
    while True:
        yield b
        a,b = b,a+b

#使用循环语句
def fb(n):
  l = []
  for i in range(1,n+1):
    if i in (1,2):
      l.append(1)
    else:
      l.append(l[i-2]+l[i-3])
    
  return l[i-1]

#使用递归函数（会导致栈溢出）
def fb(n):
  if n in (1,2):
    return 1
  else:
    return fb(n-1)+fb(n-2)
    
#通过前面元素推导下一元素
def fib(n):
  z,a,b = 0,0,1  #定义第一个元素b = 1. 其前面一个值为0（确保下一值为1）
  while z < n:   
    print (b)    
    a,b = b,a+b  #交换值，前一个值用后一个值取代；后一个值用前两值之和
    z += 1
