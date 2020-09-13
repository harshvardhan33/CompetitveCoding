# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 16:50:31 2020

@author: harshvardhan
"""
from collections import deque
arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
k = 3
q = deque()

for i in range(k):
    while len(q)>0 and q[-1]<=arr[i]:
        q.pop()
    q.append(i)

for i in range(k,len(arr)):
    print(arr[q[0]])
    
    while len(q)>0 and q[0]<=i-k:
        q.popleft()
    
    while len(q)>0 and arr[q[-1]]<=arr[i]:
        q.pop()
    
    q.append(i)
    
