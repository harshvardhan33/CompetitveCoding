# -*- coding: utf-8 -*-
"""
Created on Sat May 22 19:42:51 2021

@author: harshvardhan
"""

"""
Take an element only once 
Also show result in sorted order
"""


import copy
def solve1(idx,target,res,r,arr):
    if idx==len(arr):
        if target==0:
            temp = copy.deepcopy(r)
            # or temp = r[:]
            res.append(temp)
        return 
    if arr[idx]<=target:
        # Include
        r.append(arr[idx])
        solve1(idx+1,target-arr[idx],res,r,arr)
        r.pop(-1)
    
    # call for next index when not included
    solve1(idx+1,target,res,r,arr)
    
       
    

def solve(arr,target,res,r,i):
    # Creating a copy of elements in result
    if target==0:
        temp = r[:]
        res.append(temp)
        return
    # When target goes too low 
    if target<0:
        return 
    # check for all possibilities 
    while i<len(arr) and target-arr[i]>=0:
        r.append(arr[i])
        solve(arr,target-arr[i],res,r,i+1)
        i+=1
        r.pop(-1)
        
        
arr = [2,4,6,8]
target = 8 
res = []
r = []
solve(arr,target,res,r,0)
print("Method 1 ",res)
res = []
r = []
solve1(0,target,res,r,arr)
print("Method 2 ",res)
