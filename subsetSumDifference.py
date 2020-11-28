# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 22:28:27 2020

@author: harshvardhan
"""

arr = [1,4,2,3]
s = sum(arr)
dp = [[0 for i in range(s+1)] for j in range(len(arr)+1)]

for i in range(len(dp[0])):
    dp[0][i] = 0
for i in range(len(dp)):
    dp[i][0]=1
for i in range(1,len(dp)):
    for j in range(1,len(dp[0])):
        if arr[i-1]<=j:
            dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
        else:
            dp[i][j] = dp[i-1][j]
            

target = float("inf")

for i in range((s//2)+1):
    if dp[-1][i]==1:    
        target = min(target,s-2*i)
    