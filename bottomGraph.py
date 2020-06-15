# -*- coding: utf-8 -*-
"""
Created on Fri May 22 10:01:56 2020

@author: harshvardhan
"""


def dfs(g,n,start,visited,temp):
    temp.append(start)
    print(start)
    visited[start]=1
    for i in range(n):
        if i == start:
            continue
        if g[start][i]==1:
            if visited[i]==1:
                continue
            dfs(g,n,i,visited,temp)
            
    

def graphPrint(g,n,start,visited):
    visited[start]=1
    for i in range(n):
        if i == start:
            continue
        if g[start][i]==1:
            if visited[i]==1:
                continue
            graphPrint(g,n,i,visited)
        stack.append(start)
    

n = int(input("Enter number of vertices "))
g = [[0 for i in range(n)]for j in range(n)]
g_T = [[0 for i in range(n)]for j in range(n)]
visited =[0]*n
visited_T = [0]*n
e = int(input("Enter Edges "))
stack = []
while e:
    e-=1
    f,s = map(int,input().split())
    g[f-1][s-1] =1
    g_T[s-1][f-1] =1

count = 0


for i in range(len(visited)):
    if visited[i]==0:
        count+=1
        print("Component" + str(count))
        graphPrint(g, n, i, visited)

        
    
    
        
print("Number of components are : ",count)

print("Strongly Connected Components are")
ct = 0
cc =[]
while(len(stack)>0):
    temp = []
    ele = stack.pop()
    if visited_T[ele]==1:
        continue
    ct+=1
    dfs(g_T, n, ele, visited_T,temp)
    cc.append(temp)
    print("-------")
    
print("Total Strongly connected components are : ",ct)

c = 0
for i in range(len(cc)):
    curr = cc[i]
    for j in curr:
        for k in range(n):
            if g[j][k]==1:
                if (j in curr) and (k in curr):
                    c+=1
                else:
                    break
