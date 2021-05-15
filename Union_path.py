# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 10:06:43 2021

@author: harshvardhan
"""

def get(ele):
    # Log N complexity when rank is used 
    # N when rank is not used 
    # If you are the parent itself
    if parent[ele]==ele:
        return ele
    else:
        parent[ele] = get(parent[ele])
        return parent[ele]

def UnionRank(a,b,parent,rank):
    # Log N complexity 

    if rank[a]==rank[b]:
        rank[a]+=1
    if rank[a]>rank[b]:
        parent[b] = a
    else:
        parent[a] = b
    

def Union(a,b,parent):
    # N complexity in worst case
    pp_a = get(a) 
    pp_b = get(b)
    parent[pp_a] = pp_b
    

v = int(input("Enter Number of Vertices : "))
e = int(input("Enter Number of Edges : "))
graph = {}


for i in range(e):
    e1,e2 = map(int,input().split())
    if e1 not in graph:
        graph[e1]=[e2]
    else:
        graph[e1].append(e2)       

# Without using Rank
print("Without using rank")
parent = [i for i in range(v)]
for vertex in graph:
    for adjacent_vertex in graph[vertex]:
        p_a = get(vertex)
        p_b = get(adjacent_vertex)
        if p_a==p_b:
            print("Yes Cycle")
            break 
        else:
            Union(p_a,p_b,parent)

# With using rank 
print("With using rank")
parent = [i for i in range(v)]
rank = [0 for i in range(v)]

for vertex in graph:
    for adj_vertex in graph[vertex]:
        u_p = get(vertex)
        v_p = get(adj_vertex)
        if u_p==v_p:
            print("Yes Cycle")
            break 
        else:
            UnionRank(u_p,v_p,parent,rank)
            

        
