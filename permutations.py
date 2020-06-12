# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 14:12:04 2019

@author: harshvardhan
"""


import random
import math
import itertools



perm = []
a = []
while(len(perm)<math.factorial(len(a))):
    res = []
    while(len(res)<len(a)):
        x = random.choice(a)
        if x not in res:
            res.append(x)
    if res not in perm:
        perm.append(res)
            
print(*perm)

p = itertools.permutations(a)