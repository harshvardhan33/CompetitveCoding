# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 18:52:05 2020

@author: harshvardhan
"""
#      low
#      mid                              high
arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]

low= 0 
high = len(arr)-1
mid = 0

    
while mid<=high:
    if arr[mid]==0:
        arr[low],arr[mid] = arr[mid],arr[low]
        mid+=1
        low+=1
        continue        
    if arr[mid]==1:
        mid+=1
        continue        
    if arr[mid]==2:
        arr[high],arr[mid] = arr[mid],arr[high]
        high-=1
        continue
    