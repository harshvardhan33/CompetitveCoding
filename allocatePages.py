# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 11:41:22 2020

@author: harshvardhan
"""

def isValid(arr,mid,k):
    s = 1 
    curr = 0 
    for i in range(len(arr)):
        curr+=arr[i]
        if curr>mid:
            s+=1
            curr = arr[i]
        if s>k:
            return False
    return True


arr =[ 12, 34, 67, 90 ]
k = 2
left = 0 
right = sum(arr)
res = -1
while left<=right:
    mid = (left+right)//2
    if isValid(arr,mid,k):
        res = mid
        right = mid-1
    else:
        left = mid+1
        
print(res)