# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 20:19:32 2020

@author: harshvardhan
"""


arr = [1,2,3,4,8,10,10,12,19]
target =14
left = 0 
right = len(arr)-1
while left<=right:
    if target<arr[0]:
        res = arr[0]
        break
    mid = (left+right)//2
    if arr[mid]>=target:
        res = arr[mid]
        right = mid-1 
    else:
        left = mid+1
print(res)
    