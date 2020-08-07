# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 10:27:44 2020

@author: harshvardhan
"""

def solve(arr,i,j):
    if i>=j:
        return 0 
    ans = float("inf")
    for k in range(i,j):
        tempAns = solve(arr,i,k)+solve(arr,k+1,j)+arr[i-1]*arr[k]*arr[j]
        
        if tempAns<ans:
            ans = tempAns
    return ans

arr = [40,20,30,10,30]

print(solve(arr,1,len(arr)-1))