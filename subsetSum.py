# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 22:33:00 2020

@author: harshvardhan
"""




arr = [2,3,7,8,10]
t = 4
n = len(arr)
dp = [[False for i in range(t+1)]for j in range(n+1)]
for i in range(n+1):
    dp[i][0]=True
    
for i in range(n+1):
    for j in range(t+1):
        if arr[i-1]<=j:
            dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j]
            
print(dp[-1][-1])