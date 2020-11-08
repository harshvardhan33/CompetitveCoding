# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 20:45:17 2020

@author: harshvardhan
"""



def dfs(graph,curr):
    visited[curr]=1
    for i  in range(len(graph[0])):
        if visited[i]==0 and graph[curr][i]==1:
            dfs(graph,i)            
    st.append(curr)

def dfs2(graph,curr):
    print(curr)
    visited[curr]=1
    for i  in range(len(graph[0])):
        if visited[i]==0 and graph[curr][i]==1:
            dfs2(graph,i)            
    



graph = [[0,1,0,0,0,0,0,0],
         [0,0,1,0,0,0,0,0],
         [1,0,0,1,0,0,0,0],
         [0,0,0,0,1,0,0,0],
         [0,0,0,0,0,1,0,1],
         [0,0,0,0,0,0,1,0],
         [0,0,0,0,1,0,0,1],
         [0,0,0,0,0,0,0,0],
         ]

st = []
visited = [0 for i in range(len(graph))]
dfs(graph,0)

for i in range(len(graph)):
    for j in range(len(graph[0])):
       temp=graph[i][j]
       graph[i][j] = graph[j][i]
       graph[j][i] = temp

visited = [0 for i in range(len(graph))]
while len(st):
     temp = st.pop(0)
     if visited[temp]==0:
         print("SCC")
         dfs2(graph,temp)