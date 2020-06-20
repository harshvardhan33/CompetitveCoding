# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 14:59:54 2020

@author: harshvardhan
"""



arr = [15,13,12,14,16,8,6,4,10,30]
res = [1 for i in range(len(arr))]
stack = []
stack.append(0)


for i in range(1,len(arr)):
    while len(stack)>0 and arr[stack[-1]]<=arr[i]:
        stack.pop()
    if len(stack)==0:
        span = i+1
    else:
        span = i - stack[-1]
    print(span)
    stack.append(i)