# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 15:21:09 2020

@author: harshvardhan
"""
a = [1,3,2]

if sorted(a)[::-1]== a:
    print("Not possibel")
    
for i in range(len(a)-1,0,-1):
    if a[i-1]>=a[i]:
        continue
    else:
        break 

idx = i-1 
ele = a[idx]

for i in range(len(a)-1,-1,-1):
    if a[i]>=ele:
        break

swapIdx = i
a[swapIdx],a[idx] = a[idx],a[swapIdx]
a = a[:idx+1] + sorted(a[idx+1:])
