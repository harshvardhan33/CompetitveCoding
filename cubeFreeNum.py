# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 11:30:01 2020

@author: harshvardhan
"""




n = 50
nums = [True for i in range(n+1)]

for i in range(2,len(nums)):
    if nums[i]==True:
        x = i 
        start = x**3
        while start<n+1:
            nums[start]=False
            start = start*x
    
for i in range(1,len(nums)):
    if nums[i]==True:
        print(f"{i} : Cube Free Num")
    else:
        print(f"{i} : Not Cube Free")
        