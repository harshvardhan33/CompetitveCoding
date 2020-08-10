# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 22:12:26 2020

@author: harshvardhan
"""

"""
Problem Statement 

You can assing +/- to the array elements 
and you need to tell how many sub arrays can generate the
given target sum 


example :
    arr = [1,1,2,3]
    target = 1
    
    3 as the answer
    1 -> (1,1,2)  (3)
    2 -> (1,2)    (1,3)
    3 -> (1,2)    (1,3)
    
"""
arr = [1,1,2,3]
total_sum =  sum(arr)
diff = 1

target = int((diff+sum(arr))/2)
dp = [[0 for i in range(target+1)]for j in range(len(arr)+1)]

for i in range(len(dp)):
    dp[i][0] = 1
    

for i in range(1,len(arr)+1):
    for j in range(1,target+1):
        if arr[i-1]<=j:
            dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]]
        else:
            dp[i][j] = dp[i-1][j] 

print(dp[-1][-1])