# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 15:18:00 2020

@author: harshvardhan
"""


arr = [20,30,10,5,15]
stack = []
stack.append(arr[0])
print(-1)
for i in range(1 ,len(arr)):
    while len(stack)>0 and stack[-1]<=arr[i]:
        stack.pop()
    if len(stack)==0:
        span =-1
    else:
        span = stack[-1]
    print(span)
    stack.append(arr[i])