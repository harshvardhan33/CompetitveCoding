# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 13:24:18 2020

@author: harshvardhan
"""
# Only one single transaction can be done 
arr = [7,1,5,3,6,4]
profit = 0
mn = arr[0]

for i in range(len(arr)):
    profit = max(profit,arr[i]-mn)
    mn = min(mn,arr[i])