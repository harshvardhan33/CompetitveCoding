# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 00:11:08 2020

@author: harshvardhan
"""

arr= [1,-10,2,3]

msf = float("-inf") 
meh =  0 
start = 0
end = 0
s = 0
ans = [None,None]
for i in range(len(arr)):
    meh+=arr[i]
    if meh<0:
        meh = 0
        s = i+1
        continue
    
    if meh>msf:
        msf = meh
        start = s
        end = i
        ans = [start,end]