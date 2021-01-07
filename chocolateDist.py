# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 22:21:08 2020

@author: harshvardhan
"""

arr = [12, 4, 7, 9, 2, 23, 25, 41,30, 40, 28, 42, 30, 44, 48, 43, 50]
m = 7 
arr.sort()

i = 0
j = m-1
minDif = float("inf")
pair = [i,j]

while j<len(arr):
    if minDif>arr[j]-arr[i]:
        minDif = arr[j]-arr[i]
        pair = [i,j]
    i+=1
    j+=1
    