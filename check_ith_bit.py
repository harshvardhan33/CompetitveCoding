# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 11:56:04 2020

@author: harshvardhan
"""

n=9
i=3

ans = (n)&(2**i)
if ans==2**i:
    print("Yes bit is set")
else:
    print("Nope bit is not set")