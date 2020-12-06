# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 23:08:57 2020

@author: harshvardhan
"""

arr = [10,22,9,33,21,50,41,60]

lis = [1 for i in range(len(arr)+1)]
l = [[] for i in range(len(arr))]
l[0].append(arr[0])
ans = 0
for i in range(1,len(arr)):
    for j in range(0,i):
        if arr[i]>arr[j] and lis[i]<lis[j]+1:
            lis[i] =lis[j]+1
            ans = max(ans,lis[i])
            l[i] = l[j].copy()
    l[i].append(arr[i])
    
print(ans)
print(max(l))