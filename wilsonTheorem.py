# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 10:37:37 2020

@author: harshvardhan
"""

# Wilson theorem is used to calculate (N!)modP 
# Fermet little theorem is used for help 
def fermet(a,b,m):
    res = 1
    a =a%m
    while b>0:
        if b & 1:
            res = (res*a)%m
        a = (a*a)%m
        b>>=1
    return res
def wilson(n,p):
    ans = p-1
    for i in range(n+1,p):
        ans=(ans*fermet(i, p-2, p))%p
    return ans


n = 25
p = 29
ans = wilson(n,p)
