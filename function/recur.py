#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

#杨辉三角的完美解法：
def triangles():
    L = [1]         #定义第一行
    while True:
        yield L     #返回该行
        L.append(0) #！！！在行末加0，在计算下一行时，通过加末尾的0，是首位两个数字保持不变！！！
        L = [L[i - 1] + L[i] for i in range(len(L))]

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
    
#甲子纪年
tg = list('甲乙丙丁戊己庚辛壬癸')
dz = list('子丑寅卯辰巳午未申酉戌亥')
jz = []

i = 0
j = 0

while True:
  jz.append(tg[i]+dz[j])
  if i == len(tg) - 1 and j != len(dz) - 1:
    i = 0
  else:
    i += 1
  if j == len(dz) - 1 and i != len(tg) - 1:
    j = 0
  else:
    j += 1
  if i == len(tg) - 1 and j == len(dz) - 1:
    jz.append(tg[i]+dz[j])
    break

#Fibonacci数列生成的几中方式
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
