# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 20:39:40 2020

@author: harshvardhan
"""

arr = [4,2,2,6,4]
k = 6
xr = 0 
count = 0 
dc ={}
for i in range(len(arr)):
    xr = xr^arr[i]
    if xr^k in dc:
        count+=dc[xr^k]
    if xr==k:
        count+=1
    if xr in dc:
        dc[xr]+=1
    else:
        dc[xr]=1
        