# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 15:37:14 2020

@author: harshvardhan
"""



def bellmanFord(src,V):
    for i in range(V-1):
        for j in range(len(graph)):
            if dis[graph[j][0]]+graph[j][2]<dis[graph[j][1]]:
                dis[graph[j][1]]=dis[graph[j][0]]+graph[j][2]
    # Relax for one more time to check negative edge cycle
    for i in range(len(graph)):
        x = graph[i][0]
        y = graph[i][1]
        wt = graph[i][2]        
        if dis[x]!=float("inf") and dis[x]+wt<dis[y]:
            return False
        else:
            return True
                
V = int(input("Enter Number of vertices : "))
e = int(input("Enter Number of edges : "))

graph=[]
for i in range(e):
    u,v,w = map(int,input().split())
    graph.append([u,v,w]) 

# Source vertex selection
source = 0 
# Initial distance
dis = [float("inf") for i in range(V)]
dis[source]=0  

print("Bellman Ford Algo .......")
if bellmanFord(source,V):
    print(*dis)
else:
    print("Negative edge cycle is there")

