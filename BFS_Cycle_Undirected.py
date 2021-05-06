# -*- coding: utf-8 -*-
"""
Created on Wed May  5 12:49:59 2021

@author: harshvardhan
"""

def cycleCheck():
    # Starting point of BFS 
    parent[1] = 0 
    q = []
    q.append(1)
    while len(q)>0:
        u = q.pop(0)
        for i in edges[u]:
            v = i 
            if visited[v]==0:    
                parent[v] = u
                visited[v] = 1
                q.append(v)
            elif parent[u]!=v:
                return True
    return False

v,e = map(int,input().split())
visited = [0 for i in range(v+1)]
parent = [-1 for i in range(v+1)]

edges = {i+1:[] for i in range(v)}

for i in range(e):
    e1,e2 = map(int,input().split())
    edges[e1].append(e2)
    edges[e2].append(e1)
    

if cycleCheck():
    print("Yes there is a cycle")
else:
    print("No cycle")
