# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 19:50:25 2021

@author: tiankuan
"""

#2.1生成5×10和10×5的两个取值于0-50随机数的矩阵

import numpy as np
M1 = np.random.randint(0,51,[5,10])
M2 = np.random.randint(0,51,[10,5])
print(M1,'\n',M2)

#2.2计算生成的两个矩阵的乘积
def Matrix_multip(M1,M2):
    multi_list=[]
    for i in range(len(M1)):
        temp=[]
        for k in range(len(M1)):
            multip=0
            for j in range(len(M2)):
                multip+=((M1[i][j]))*((M2[j][k]))
            temp.append(multip)
        multi_list.append(temp)
    M = np.array(multi_list)
    print(M)

#举例如下：
import numpy as np
M1 = np.random.randint(0,51,[5,10])
M2 = np.random.randint(0,51,[10,5])
print(M1,'\n',M2)
Matrix_multip(M1,M2)