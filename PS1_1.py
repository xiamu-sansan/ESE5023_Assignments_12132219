# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 10:29:55 2021

@author: tiankuan
"""

#生成三个0到100中的随机数#

import random

a = round(random.random()*100)
b = round(random.random()*100)
c = round(random.random()*100)

print(a, b, c)

#比较这三个数的大小#

if a > b:
    if b > c:
        print(a, b, c)
    elif a > c:
        print(a, c, b)
    else:
        print(c, a, b)
elif not(b > c):
    print(c, b, a)
else:
    print("b is the maximum value")