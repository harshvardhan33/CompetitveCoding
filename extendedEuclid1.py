# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 14:45:41 2021

@author: harshvardhan
"""

def extendedEuclid(a,b,):
    if b==0:
        return 1,0,a
    t1,t2,t3 = extendedEuclid(b, a%b)
    # x = t2
    # y = t1 - (a//b)*t2
    return t2,t1 - (a//b)*t2,t3
a = 5
b = 17
print(extendedEuclid(a, b))