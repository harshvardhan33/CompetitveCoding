# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 12:42:17 2021

@author: harshvardhan
"""

arr = [1, 1, 0, 0, 1, 0, 1, 0,1, 1, 1] 

count = 0 
curr = 0
for i in range(len(arr)):
    if arr[i]==0:
        curr = 0 
    else:
        curr+=1
    count = max(curr,count)

print(count)