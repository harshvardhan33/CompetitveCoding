# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 09:59:12 2019

@author: harshvardhan
"""

ls = [1,5]
tg = 6
res = []
for i in range(tg+1):
    for j in range(tg+1):
        if i*1 + j*5 == tg :
            res.append((i*1,j*5))    