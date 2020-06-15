# -*- coding: utf-8 -*-
"""
Created on Thu May 14 10:05:16 2020

@author: harshvardhan
"""
def graphPrint(g,n,start,visited):
    seen = []
    seen.append(start)
    visited[start]=1
    while(len(seen)>0):
        curr = seen.pop(0)
        print(curr)
        for i in range(n):
            if g[curr][i]==1 and visited[i]==0:
                seen.append(i)
                visited[i]=1
                
    
            
n = int(input("Enter number of vertices "))
g = [[0 for i in range(n)]for j in range(n)]
visited =[0]*n
e = int(input("Enter Edges "))

while e:
    e-=1
    f,s = map(int,input().split())
    g[f][s] =1
    g[s][f] =1

count = 0
for i in range(len(visited)):
    if visited[i]==0:
        count+=1
        graphPrint(g, n, i, visited)