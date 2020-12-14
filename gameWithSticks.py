# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 22:02:29 2020

@author: harshvardhan
"""

n,m = map(int,input().split())
c = 0 
while n and m:
    n-=1
    m-=1
    if c==0:
        c=1
    else:
        c=0
if c:
    print("Akshat")
else:
    print("Malvika")