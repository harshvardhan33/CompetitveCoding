# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:41:57 2020

@author: harshvardhan
"""



coins = [1,2,3]
n = len(coins)
amount = 5
dp = [[0 for i in range(amount+1)]for j in range(n+1)]
for i in range(n+1):
    dp[i][0]=1
for i in range(1,n+1):
    for j in range(1,amount+1):
        if coins[i-1]<=j:
            dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
        else:
            dp[i][j] = dp[i-1][j]
            