# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 21:42:38 2020

@author: harshvardhan
"""

arr = [15, -2, 2, -8, 1, 7, 10, 13] 

max_len =0 
sm = 0 
dc={}
for i in range(len(arr)):
    sm+=arr[i]
    
    if arr[i]==0 and max_len==0:
        max_len = 1
    
    if sm==0:
        max_len = i+1
        
    if sm in dc:
        max_len = max(max_len,i-dc[sm])
    else:
        dc[sm]=i
    
    