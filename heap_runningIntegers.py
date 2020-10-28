# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 18:33:41 2020

@author: harshvardhan
"""
import heapq
arr = [5,15,1,3]
q1 = [] # max heap
q2 = [] # min heap 
heapq.heapify(q1)
heapq.heapify(q2)
for i in range(len(arr)):
    if len(q1)==0 or q1[0]>arr[i]:
        heapq.heappush(q1,-1*arr[i])
    else:
        heapq.heappush(q2, arr[i])
   # Maintain the difference of atmost 1 in sizes 
    if len(q1)>len(q2)+1:
        temp = heapq.heappop(q1)
        heapq.heappush(q2, temp)
    elif len(q2)>len(q1)+1:
        temp = heapq.heappop(q2)
        heapq.heappush(q1, -1*temp)
    if len(q1)==len(q2):
        print(((-1*q1[0])+q2[0])/2)
    else:
        if len(q1)>len(q2):
            print(-1*q1[0])
        else:
            print(q2[0])
