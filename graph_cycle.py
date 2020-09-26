# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 13:49:35 2020

@author: harshvardhan
"""



def dfs(v,vis,re_vis,graph):
    vis[v]=1
    re_vis[v]=1
    for neighbour in graph[v]:
        if vis[neighbour]==False:
            if dfs(neighbour, vis, re_vis, graph):
                return True
        elif re_vis[neighbour]==True:
            return True
    re_vis[v] = 0
    return False


v = int(input("Number of vertices : "))
e = int(input("Number of edges : "))
graph= {i:[] for i in range(v)}
for i in range(e):
    e1,e2 = map(int,input().split())
    graph[e1].append(e2)



vis= [0 for i in range(v)]
re_vis = [0 for j in range(v)]
flag = 0 
for i in range(len(vis)):
    if vis[i]==0:
        if (dfs(i,vis,re_vis,graph)):
            flag = 1
            break
if flag:
    print("Yup Cycle")
else:
    print("Nope Cycle")


