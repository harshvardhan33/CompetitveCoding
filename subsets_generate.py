# -*- coding: utf-8 -*-
"""
Created on Mon May 24 10:02:20 2021

@author: harshvardhan
"""

"""
We need to print the subsets possible
Pick and Choose elements in such a way 
that you avoid the duplicates.
"""

import copy

def subsetSum2(idx,arr,r,res):
    temp = copy.deepcopy(r) # or temp = r[:]
    # Pick the element
    res.append(temp)
    for i in range(idx,len(arr)):
        if i!=idx and arr[i]==arr[i-1]:
            continue 
        r.append(arr[i])
        subsetSum2(idx+1,arr,r,res)
        r.pop(-1)



arr = [1,2,2]
res = []
r = []
target = 4
subsetSum2(0,arr,r,res)
print(res)