# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 00:02:45 2020

@author: harshvardhan
"""

"""
The aim is to find the longest common char in string 
example - "AABCDDBBBA"
answer - {B:3}
"""


def LongestCommonChar(st):
    count = 1
    maxCount = 0
    dc = {}
    for i in range(1,len(st)):
        current = st[i]
        prev = st[i-1]
        if current == prev:
            count+=1
        else:
            count=1
        if count>=maxCount:
            maxCount=count
            dc[st[i]]=maxCount
        
    for i,j in dc.items():
        if j==maxCount:
            return {i:maxCount}
    
    
    

    
st = "AABCDDBBBA"
print(LongestCommonChar(st))
