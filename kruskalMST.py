# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 14:17:14 2020

@author: harshvardhan
"""

def findParent(parent,i):
    if parent[i]==i:
        return i 
    return findParent(parent,parent[i])

def union(parent,rank,x,y):
    x_p = findParent(parent,x)
    y_p =findParent(parent,y)
    if rank[x_p]<rank[y_p]:
        parent[x_p] = y_p
    elif rank[x_p]>rank[y_p]:
        parent[y_p] = x_p
    else:
        parent[y_p] = x_p
        rank[x_p]+=1
    
V = int(input("Enter number of vertices : "))
e = int(input("Enter number of edges : "))
graph = []
while e:
    e-=1
    u,v,w = map(int,input().split())
    graph.append([u,v,w])

graph.sort(key = lambda x:x[2])   
result = []
parent = []
rank = []
for i in range(V):
    parent.append(i)
    rank.append(0)
e = 0
i=0
while e<V-1:
    u,v,w = graph[i]
    i=i+1
    x = findParent(parent,u)
    y = findParent(parent,v)
    if x!=y:
        e+=1
        result.append([u,v,w])
        union(parent,rank,x,y)
ans = 0
for u,v,w in result:
    ans+=w
print(ans)