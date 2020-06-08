# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 09:42:53 2019

@author: harshvardhan
"""


arr = [0,8,0,0,5,0,0,10,0,0,1,1,0,3]
 
leftMaxArr = [0 for x in arr]
rightMaxArr = [0 for x in arr]
water = [0 for x in arr]
leftmax=rightmax=0

for i in range(len(arr)):
    height = arr[i]
    leftMaxArr[i] = leftmax
    leftmax = max(leftmax,height)
    
for i in reversed(range(len(arr))):
    height = arr[i]
    rightMaxArr[i] = rightmax
    rightmax = max(rightmax,height)
    

for i in range(len(arr)):
    minHeight = min(leftMaxArr[i],rightMaxArr[i])
    if arr[i] < minHeight:
        water[i] = minHeight - arr[i]

print(sum(water))