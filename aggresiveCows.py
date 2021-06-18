# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 13:05:53 2021

@author: harshvardhan
"""

def check(dist,arr):
    co_ord = arr[0]
    c = 1
    for i in range(1,len(arr)):
        if arr[i]-co_ord>=dist:
            c+=1
            co_ord = arr[i]
        if c==cow:
            return True 
    return False

arr = [1,2,4,8,9]
left = 1
right = max(arr)
cow = 3
res = -1
while left<=right:
    mid = (left+right)//2
    if check(mid,arr):
        res = mid 
        left = mid+1
    else:
        right = mid-1

print(res)