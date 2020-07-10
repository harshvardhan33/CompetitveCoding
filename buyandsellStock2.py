# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 13:24:39 2020

@author: harshvardhan
"""

# Multiple transactions are allowed

arr = [7,1,5,3,6,4]

profit = 0 

for i in range(1,len(arr)):
    if arr[i]>=arr[i-1]:
        print(arr[i-1],arr[i])
        profit+=arr[i]-arr[i-1]