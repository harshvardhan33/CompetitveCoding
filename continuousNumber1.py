# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 21:28:36 2020

@author: harshvardhan
"""



arr = [1,1,0,0,1,0,1,0,1,1,1,1]
msf = float('-inf')  
meh = 0 
s = 0
index = [None,None]
for i in range(len(arr)):
    meh+=(-1 if arr[i]==0 else 1)
    if meh<0:
        meh=0
        s = i+1
        continue
    if msf<meh:
        msf = meh
        index = [s,i]