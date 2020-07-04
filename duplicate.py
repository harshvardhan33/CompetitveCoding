# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 12:30:28 2020

@author: harshvardhan
"""

a = [1,3,4,2,2]
dc = {}
for i in a:
    if i not in dc:
        dc[i] = 1
    else:
        print(i)
        break