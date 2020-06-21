# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 12:18:34 2020

@author: harshvardhan
"""


def extEuclid(a,b):
    if b==0:
        return a,1,0
    
    gcd,x1,y1 = extEuclid(b,a%b)
    x=y1
    y=x1 - (a//b)*y1
    return gcd,x,y



a,b=5,17
g,x,y = extEuclid(a,b)
