# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 21:33:19 2020

@author: harshvardhan
"""

a = [[1,0,1],[1,1,1],[1,1,1]]
row = [False,False,False]
col = [False,False,False]

for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j]==0:
            row[i]=True
            col[j]=True


for i in range(len(a)):
    for j in range(len(a[0])):
        if row[i]==True or col[j]==True:
            a[i][j] = 0
