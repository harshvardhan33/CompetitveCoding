# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 20:22:56 2020

@author: harshvardhan
"""

def solve(arr,l,r,count,x):
    if x==0:
        return count 
    if x<0 or l>r:
        return float("inf")
    key = str(l)+"*"+str(r)+"*"+str(x)
    if key in dc:
        return dc[key]
    left = solve(arr,l+1,r,count+1,x-arr[l])
    right = solve(arr,l,r-1,count+1,x-arr[r])
    dc[key] = min(left,right)
    return dc[key]   


arr = [1,1,4,2,3]
X =5
dc = {}
print(solve(arr,0,4,0,X))

