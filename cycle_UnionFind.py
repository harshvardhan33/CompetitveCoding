# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 00:19:24 2020

@author: harshvardhan
"""


def find_parent(i):
    if parent[i]==-1:
        return i
    if parent[i]!=-1:
        return find_parent(parent[i])



V = int(input("Enter Number of vertices : "))
e = int(input("Enter Number of edges : "))

# using dictionary for graph
graph = {}
parent = [-1 for i in range(V)]
for i in range(e):
    e1,e2 = map(int,input().split())
    if e1 not in graph:
        graph[e1] = [e2]
    else:
        graph[e1].append(e2)

for v in graph:
    for adj_v in graph[i]:
        x = find_parent(v)
        y = find_parent(adj_v)
        if x==y:
            print("Yes Cycle")
            break
        x_set_p = find_parent(x)
        y_set_p = find_parent(y)
        parent[x_set_p] = y_set_p        
        
    



