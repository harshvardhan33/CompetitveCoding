# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 19:20:32 2020

@author: harshvardhan
"""



arr =[100, 4, 200, 1, 3, 2]
dc=  {}
for i in arr:
    if i not in dc:
        dc[i]=1        
mx = float("-inf")
for i in arr:
    curr = i 
    left = i-1 
    right = i+1
    while left in dc:
        left-=1
    while right in dc:
        right+=1    
    mx = max(mx,right-(left+1))
    print(left+1,right)
    