# -*- coding: utf-8 -*-
"""
Created on Sat May 16 15:27:11 2020

@author: harshvardhan
"""


g = [[0,1,1,1,0],[1,0,0,1,1],[1,0,0,1,0],[1,1,1,0,1],[0,1,0,1,0]]

count = 0
for i in range(3):
    for j in range(3):
        for k in range(3):
            if i==k or i==j or j==k:
                continue
            if g[i][j]==1 and g[j][k]==1 and g[k][i]==1:
                count+=1