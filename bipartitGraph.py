# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 14:19:32 2020

@author: harshvardhan
"""


def isBipartite(g,color,v,src):
    q = []
    q.append(src)
    color[src]=1
    while len(q)>0:
        u = q.pop()
        for i in range(v):
            if g[u][i]==1 and color[i]==-1:
                color[i] = 1-color[u]
                q.append(i)
            elif g[u][i]==1 and color[i]==color[u]:
                return False
    return True

v,e = map(int,input().split())
g = [[0 for i in range(v)]for j in range(v)]

color = [-1 for i in range(v)]

for i in range(e):
    e1,e2 = map(int,input().split())
    g[e1-1][e2-1] = 1
    g[e2-1][e1-1] = 1
    
  
print(isBipartite(g,color,v,0))