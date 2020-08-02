# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 19:33:52 2020

@author: harshvardhan
"""



length = [1,2,3,4,5,6,7,8]
prices = [1, 5, 8, 9, 10, 17, 17, 20] 
n = 8

t = [[0 for i in range(8+1)]for j in range(8+1)]


for i in range(1,8+1):
    for j in range(1,8+1):
        if length[i-1]<=j:
            t[i][j] = max(prices[i-1]+t[i][j-length[i-1]],t[i-1][j])
        else:
            t[i][j] = t[i-1][j]             
            
    
print(t[-1][-1])