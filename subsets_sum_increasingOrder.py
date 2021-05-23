# -*- coding: utf-8 -*-
"""
Created on Sun May 23 11:12:59 2021

@author: harshvardhan
"""

"""
Approach 1 : Power Set 
This is the brute force approach 
Complexity :  2^n*n

Approach 2 :
This is the efficient/optimal approach 

 
"""

def subsetSum(idx,sm,arr,N,subset):
    if idx==N:
        subset.append(sm)
        return 
    # Pick 
    subsetSum(idx+1,sm+arr[idx],arr,N,subset)
    # Not Pick
    subsetSum(idx+1,sm,arr,N,subset)
    

N = 2
arr = [2,3]
subset = []
subsetSum(0,0,arr,N,subset)
print(sorted(subset))