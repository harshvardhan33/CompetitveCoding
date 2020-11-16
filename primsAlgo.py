# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 19:51:52 2020

@author: harshvardhan
"""

def getMin(dist,set_MST):
    mn = float("inf")
    idx =None
    for i in range(V):
        if dist[i]<mn and set_MST[i]==0:
            mn = dist[i]
            idx = i
    return idx

V = int(input("Enter number of vertices : "))
graph = [[0, 2, 0, 6, 0], 
         [2, 0, 3, 8, 5], 
         [0, 3, 0, 0, 7], 
         [6, 8, 0, 0, 9], 
         [0, 5, 7, 9, 0]] 
"""
e = print("Enter Number of edges")
graph = [[0 for i in range(V)]for j in range(V)]
for i in range(e):
    e1,e2,w = map(int,input().split())
    graph[e1][e2]=w
    graph[e2][e1]=w
"""
  
dist = [float("inf") for i in range(V)]
set_Mst = [0 for i in range(V)] # track of nodes in MST
parent = [None for i in range(V)] # track MST structure

# Initial values 
dist[0] = 0 # starting vertex
parent[0] = -1 # source node no parent


print("Prims Algorithm Begins----")

for i in range(V):
    u = getMin(dist,set_Mst)
    set_Mst[u]=1
    for v in range(V):
        if graph[u][v]>0 and set_Mst[v]==0 and dist[v]>graph[u][v]:
            dist[v] = graph[u][v]
            parent[v] = u

print("Mst Values : ")

for i in range(1,V):
    print(parent[i],"-",i," : ", graph[i][parent[i]])
    

