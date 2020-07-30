# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 19:44:46 2020

@author: harshvardhan
"""

def isSafe(curr,color,n):
    for i in range(n):
        if graph[curr][i]==1 and v_color[i]==color:
            return False
    return True  

def isColorable(curr,k,n):
    if curr==n:
        return True
    for color in range(1,k+1):
        if isSafe(curr,color,n):
            v_color[curr]=color
            if isColorable(curr+1,k,n):
                return True
            v_color[curr]=0
    return False

vertices = 4
graph = [[0 for i in range(vertices)]for j in range(vertices)]
v_color = [0 for i in range(vertices)]
edges = 5
k = 3
for i in range(edges):
    e1,e2 = map(int,input().split())
    graph[e1][e2]=1
    graph[e2][e1]=1
if isColorable(0,k,vertices)==True:
    print("Yes Colorable")
    print(*v_color)
else:
    print("Not Colorable")
