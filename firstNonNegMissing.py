# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 20:53:52 2020

@author: harshvardhan
"""

arr= [3,2,5,1]

for i in range(len(arr)):
    while arr[i]<len(arr) and arr[i]!=i+1:
        temp = arr[i]
        arr[i] = arr[temp-1]
        arr[temp-1] = temp

for i in range(len(arr)):
    if arr[i]!=i+1:
        print(i+1)
        break