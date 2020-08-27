# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 18:51:51 2020

@author: harshvardhan
"""

def mooreAlgo(arr):
    ele = 0 
    count= 0 
    for i in arr:
        if count==0:
            ele = i
        if ele==i:
            count+=1
        else:
            count-=1
    
    return ele

def hashing(arr):
    dc = {}
    ans = None
    for i in arr:
        if i not in dc:
            dc[i]=1
        else:
            if dc[i]>=len(arr)//2:
                ans = i
                break
            dc[i]+=1
    return ans,dc
            



arr = [7,7,5,7,5,1,5,7,5,5,7,7,5,5,5,5]
ans,dc  = hashing(arr)
print(ans)

print(mooreAlgo(arr))