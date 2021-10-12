# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 17:21:08 2021

@author: tiankuan
"""


#求帕斯卡三角第k行
#定义一个函数，利用中间的任何一个数都等于上一行同序列数字加其前一个数字性质。

def Pascal_triangle(k):
    tri = [1]
    while True:
        yield tri
        h = len(tri) - 1
        mid = []
        i = 0
        while i < h:
            mid.append(tri[i]+tri[i+1])
            i = i + 1
        tri = [1] + mid + [1]
        if i + 1 == k:
            break
#使用函数report k=100和k=200 的结果
n = 0
k = int(input("please input an int(such as 100 or 200):"))
for t in Pascal_triangle(k):
    n = n + 1
    if n == k:
        print(t)
        break