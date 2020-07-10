# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 13:24:45 2020

@author: harshvardhan
"""

arr = [3,3,5,0,0,3,1,4]

# Left Side max Profit 
mn = arr[0]
profitLeft = [0 for i in range(len(arr))]
for i in range(1,len(arr)):
    profitLeft[i] = max(profitLeft[i-1],arr[i]-mn)
    mn = min(mn,arr[i])


# Right Side max Profit 
mx = arr[-1]
profitRight = [0 for i in range(len(arr))]
for i in range(len(arr)-2,-1,-1):
    profitRight[i] = max(profitRight[i+1],mx-arr[i])
    mx = max(mx,arr[i])


# Find the max profit among 2 arrays 
answer = 0
for i,j in zip(profitLeft,profitRight):
    answer = max(answer,i+j)