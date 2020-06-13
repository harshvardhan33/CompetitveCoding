# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 17:04:49 2019

@author: harshvardhan
"""

a = 2
b = 16
count = 0
res = 1
while(b>0):
    #whenever the power is odd we enter in this loop 
    #by this technique we compute exponentiation in just logn + 1 steps
    
    count+=1
    
    if(b & 1):
        res = res*a
    a= a*a
    b>>=1
    