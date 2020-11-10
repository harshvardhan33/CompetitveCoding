# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 19:03:50 2020

@author: harshvardhan
"""



def minDist(dist,sptSet):
    min_dist = float("inf")
    for v in range(V):
        if dist[v]<min_dist and sptSet[v]==0:
            min_dist = dist[v]
            mn_idx = v
    return mn_idx

def dijkstra(src):
    for i in range(V):
        u = minDist(dist,path_Set)
        path_Set[u]=1
        for v in range(V):
            if graph[u][v]>0 and path_Set[v]==0 and dist[v]>dist[u]+graph[u][v]:
                dist[v] = dist[u]+graph[u][v]
    return dist
    
V = 6
graph = [[0,2,4,0,0,0],
         [0,0,1,7,0,0],
         [0,0,0,0,3,0],
         [0,0,0,0,0,1],
         [0,0,0,2,0,5],
         [0,0,0,0,0,0]]

dist = [float("inf") for i in range(V)]
src = 0     
dist[src] = 0
path_Set = [0 for i in range(V)]
print(dijkstra(src))