# -*- coding: utf-8 -*-
"""
Created on Mon May 17 11:11:00 2021

@author: harshvardhan
"""


def dfs(curr):
    visited[curr]=1
    for v in range(len(graph)):
        if graph[curr][v]==1 and visited[v]==0:
            dfs(v)


v,e = 6,7
graph = [[0 for i in range(v)] for j in range(v)]
visited= [0 for i in range(v)]
num_comp= 0
edges = []
for i in range(e):
    e1,e2 = map(int,input().split())
    graph[e1][e2] = 1
    graph[e2][e1] = 1     
    edges.append((e1,e2))

for i in range(v):
    if visited[i]==0:
        num_comp+=1
        dfs(i)

print(num_comp)
for i in edges:
    temp_count = 0
    visited = [0 for i in range(v)]

    # Exclude the edge
    graph[i[0]][i[1]] = 0
    graph[i[1]][i[0]] = 0
    
    # Check Components
    for j in range(v):
        if visited[j]==0:
            temp_count+=1
            dfs(j)
    
    # Include the Edge
    graph[i[0]][i[1]] = 1
    graph[i[1]][i[0]] = 1
    
    # Compare with original Components
    if temp_count>num_comp:
        print("Bridge : ", i)
    

        