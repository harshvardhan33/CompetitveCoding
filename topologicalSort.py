# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 20:26:16 2020

@author: harshvardhan
"""



def dfs(curr):
    visited[curr]=1
    for i in graph[curr]:
        if visited[i]==0:
            dfs(i)
    stack.append(curr)
graph = [[0,0,1,1,0,0],
         [0,0,0,0,0,0],
         [0,0,0,0,0,0],
         [0,1,0,0,0,0],
         [0,1,1,0,0,0],
         [1,0,1,0,0,0]]
visited = [0 for i in range(len(graph))]
stack = []
for i in range(len(graph)):
    if visited[i]==0:
        dfs(i)
print(stack[::-1])