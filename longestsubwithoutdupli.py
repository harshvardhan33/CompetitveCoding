# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 13:57:08 2019

@author: harshvardhan
"""

s1 = "clementisacap"
h = []
res =[]

for i in range(len(s1)):
    h.append(s1[i])
    j = i
    while s1[j+1] not in h and j<=len(s1):
        h.append(s1[j])
        j+=1
        res.append((i,j))
        del h[:]
    