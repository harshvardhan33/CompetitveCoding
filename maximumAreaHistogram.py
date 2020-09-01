# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 14:08:34 2020

@author: harshvardhan
"""

arr = [6,2,5,4,5,1,6]
n = len(arr)
right = [n for i in range(n)]
left = [-1 for i in range(n)]
stack = []
for i in range(len(arr)):
    if len(stack)==0:
        stack.append([arr[i],i])
        continue
    if len(stack)>0 and stack[-1][0]>arr[i]:
        while len(stack)>0 and stack[-1][0]>arr[i]:
            stack.pop()
        if len(stack):
            left[i] = stack[-1][1]
        stack.append([arr[i],i])
        continue
    if stack[-1][0]<arr[i]:
        left[i] = stack[-1][1]
        stack.append([arr[i],i])

stack.clear()
for i in range(len(arr)-1,-1,-1):
    if len(stack)==0:
        stack.append([arr[i],i])
        continue
    if len(stack)>0 and stack[-1][0]>arr[i]:
        while len(stack)>0 and stack[-1][0]>arr[i]:
            stack.pop()
        if len(stack):
            right[i] = stack[-1][1]
        stack.append([arr[i],i])
        continue
    if stack[-1][0]<arr[i]:
        right[i] = stack[-1][1]
        stack.append([arr[i],i])
stack.clear()
mx = 0
for i in range(n):
    mx = max(mx,arr[i]*(right[i]-left[i]-1))
    
