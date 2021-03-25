# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:30:42 2021

@author: harshvardhan
"""

arr = [8,9,10,11,12]
dc = {}
xor = 0 
k = 3
count = 0
for i in range(len(arr)):
    xor = xor^arr[i]
    if xor==k:
        count+=1
    if xor^k in dc:
        count+=dc[xor^k]
    if xor in dc:
        dc[xor]+=1
    else:
        dc[xor] =1        
        