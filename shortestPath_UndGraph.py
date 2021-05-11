# -*- coding: utf-8 -*-
"""
Created on Tue May 11 11:06:47 2021

@author: harshvardhan
"""



v,e= 9,11
graph = {0: [1, 3],1: [0, 3, 2],2: [1, 6],
         3: [0, 1, 4],4: [3, 5],5: [4, 6],
         6: [2,5,7,8],7: [6, 8],8: [7, 6]}
   

dist = [float("inf") for i in range(v)]
q = []
q.append(0)
dist[0] = 0
while len(q)>0:
    u = q.pop(0)
    for i in graph[u]:
        if dist[i]>dist[u]+1:
            dist[i] = dist[u]+1
            q.append(i)
        
        