# -*- coding: utf-8 -*-
"""
Created on Fri May 28 10:57:12 2021

@author: harshvardhan
"""

num = int(input("Enter Number : "))
root = int(input("Enter Root : "))


left = 1
right = num
eps = 1e-6

while (right-left)>eps:
    mid = (left+right)/2
    if mid**root<num:
        left = mid
    else:
        right = mid
        
print(round(mid,6))