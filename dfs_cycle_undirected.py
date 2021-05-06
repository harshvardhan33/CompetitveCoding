# -*- coding: utf-8 -*-
"""
Created on Thu May  6 11:59:49 2021

@author: harshvardhan
"""



def DFSCycle(curr,parent):
    visited[curr-1] = 1
    for u in edges[curr]:
        if visited[u-1]==0:
            if DFSCycle(u,curr):
                return True 
        elif u!=parent:
            return True
    return False
        


v,e = map(int,input().split())
visited = [0 for i in range(v)]
edges = {i+1:[] for i in range(v)}


for i in range(e):
    e1,e2 = map(int,input().split())
    edges[e1].append(e2)
    edges[e2].append(e1)
    
    
    

for i in range(1,v+1):
    if visited[i-1]==0:
        if DFSCycle(i,-1):
            print("Yes Cycle")
            break

            