# -*- coding: utf-8 -*-
"""
Created on Sat May 16 15:00:50 2020

@author: harshvardhan
"""


def graphPrint(g,n,start,visited):
    
    temp.append(start+1)
    visited[start]=1
    for i in range(n):
        if i == start:
            continue
        if g[start][i]==1:
            if visited[i]==1:
                continue
            graphPrint(g,n,i,visited)
            
    return temp
ui = [3,3,1,5,6,4]
vi = [1,2,2,4,5,6]

g = [[0 for i in range(6)]for j in range(6)]
visited =[0]*len(ui)

for i in range():
    g[ui[i]-1][vi[i]-1] = 1 
    g[vi[i]-1][ui[i]-1] = 1 

n = len(ui)
cycles = []
count = 0
for i in range(len(visited)):
    if visited[i]==0:
        temp = []
        x=graphPrint(g, n, i, visited)
        if len(x)==3:
            count+=1