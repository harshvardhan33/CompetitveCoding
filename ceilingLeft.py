# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 12:50:42 2020

@author: harshvardhan
"""

arr = [2,8,30,15,25,12]

ceil = [-1 for i in range(len(arr))]

curr=-1

for i in range(1,len(arr)):
    if arr[i]<ceil[i-1]:
        ceil[i] = -1
    ceil[i] = max(ceil[i-1],arr[i-1])