# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 20:59:11 2020

@author: harshvardhan
"""

n = 10

arr = [i for i in range(n+1)]

for i in range(2,n+1):
    if arr[i]==i:
        arr[i] = i-1
        for j in range(2*i,n+1,i):
            arr[j] = (arr[j]*(i-1))//i