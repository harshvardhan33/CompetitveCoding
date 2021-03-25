# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 21:31:37 2020

@author: harshvardhan
"""

N=15
res = []
for i in range(1,N+1):
    if i%3==0 and i%5==0:
        res.append("FizzBuzz")
        continue
    elif i%3==0:
        res.append("Fizz")
        continue
    elif i%5==0:
        res.append("Buzz")
        continue
    else:
        res.append(i)