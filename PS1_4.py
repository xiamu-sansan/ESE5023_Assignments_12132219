# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 10:57:26 2021

@author: tiankuan
"""

#从1开始+1或×2，最少的步骤得到一个1-100内的随机数
#逆向思维，从结果反推计算次数

#建立函数
def Least_moves(n):
    i = 0
    while n > 1:
        if n % 2 == 0:
            n = n/2
            i = i+1
        else:
            n = n-1
            i = i+1
    print("moves:",i)

#使用函数
import random as r
x = r.randint(1,100)
print("RMB:",x)
Least_moves(x)