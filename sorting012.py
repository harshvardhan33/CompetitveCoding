# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 12:58:33 2020

@author: harshvardhan
"""

arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1] 

z=o=t=0
for i in arr:
    if i==0:
        z+=1
    if i==1:
        o+=1
    if i==2:
        t+=1
arr =[0]*z + [1]*o + [2]*t