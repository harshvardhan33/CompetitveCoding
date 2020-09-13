# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 10:14:45 2020

@author: harshvardhan
"""

coins = [1,2,3]
target = 5
ways = [float("inf") for i in range(target+1)]
ways[0] = 0

for i in coins:
    for j in range(target+1):
        if i<=j:
            ways[j] = min(ways[j],1+ways[j-i])
            
            
dp = [[float("inf") for i in range(target+1)]for j in range(len(coins)+1)]
for i in range(len(dp)):
    dp[i][0] = 0

for i in range(1,len(dp)):
    for j in range(1,len(dp[0])):
        if i<=j:
            dp[i][j] = min(dp[i-1][j],1+dp[i][j-coins[i-1]])
        else:
            dp[i][j] = dp[i-1][j]