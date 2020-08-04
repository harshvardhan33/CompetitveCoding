# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 14:22:18 2020

@author: harshvardhan
"""





def solve(arr,target,res,r,i):
    if target==0:
        temp = r[:]
        res.append(temp)
        return

    if target<0:
        return 
    
    while i<len(arr) and target-arr[i]>=0:
        r.append(arr[i])
        solve(arr,target-arr[i],res,r,i)
        i+=1
        r.pop(-1)
        
        
arr = [2,4,6,8]
target = 8 
res = []
r = []
solve(arr,target,res,r,0)