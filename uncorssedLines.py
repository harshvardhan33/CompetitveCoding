# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 13:30:56 2020

@author: harshvardhan
"""
A = [2,5,1,2,5]
B = [10,5,2,1,5,2]

dp = [[0 for i in range(len(B)+1)]for j in range(len(A)+1)]

for i in range(1,len(A)+1):
    for j in range(1,len(B)+1):
        if A[i-1]==B[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    