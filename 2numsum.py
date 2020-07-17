# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:26:21 2020

@author: harshvardhan
"""

a = [1,2,3,4,5,16]
sm = 6

dc = {}

for i in range(len(a)):
    if sm-a[i] in dc:
        print(a[i],sm-a[i])
        dc[a[i]] = True
    else:
        dc[a[i]] = True