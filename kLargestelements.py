# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 17:51:15 2020

@author: harshvardhan
"""

import heapq
from heapq import heapify,heappush,heappop

# we build a max heap 
# we extractk items
arr = [5,15,10,20,8]


heap = []
heapify(heap)

for i in range(len(arr)):
    heappush(heap,arr[i])
    

print(heapq.nlargest(2, heap))

heap = []
heapify(heap)
for i in range(len(arr)):
    heappush(heap,-1*arr[i])
k=2
for i in range(k):
    ans = heappop(heap)
    print(-1*ans)