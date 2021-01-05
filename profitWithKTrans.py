# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 22:24:26 2021

@author: harshvardhan
"""

prices = [2,4,8,6,7]
k = int(input("Enter number of transactions : "))

dp = [[0 for i in range(len(prices))]for j in range(k+1)]


for i in range(1,len(dp)):
    for j in range(1,len(dp[0])):
        # No transaction 
        t1 = dp[i][j-1]
        # Sell on today 
        # We will have m previous transactions (0 to j-1)
        t2 = float("-inf")
        for m in range(0,j):
            t2 = max(t2,prices[j]-prices[m]+dp[i-1][m])
        dp[i][j] = max(t1,t2)


print(dp[-1][-1])
        
