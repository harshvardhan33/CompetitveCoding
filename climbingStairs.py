# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 09:43:39 2021

@author: harshvardhan
"""

def climb(n):
    if n<0:
        return 0
    if dp[n]!=-1:
        return dp[n]
    
    dp[n-1] = climb(n-1)
    dp[n-2] = climb(n-2)
    return dp[n-1]+dp[n-2]

n = 4
dp = [-1 for i in range(n+1)]
dp[0] = 1
print(climb(n))

