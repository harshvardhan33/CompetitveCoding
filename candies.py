# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 10:31:43 2020

@author: harshvardhan
"""





n = int(input())
cost =[]
for i in range(n):
    t = list(map(int,input().split()))
    cost.append(t)
dp = [0 for i in range(2**n)]
dp[0]=1
for mask in range(2**n):
    temp = mask
    count = 0
    # count the set bits
    while temp>0:
        if temp%2==1:
            count+=1
        temp = temp//2
        
    # add to the values that are affected by this mask 
        
    for j in range(n):
        if (mask&(1<<j)==0 and cost[count][j]==1):
            dp[mask|1<<j] += dp[mask]

print(dp[-1])