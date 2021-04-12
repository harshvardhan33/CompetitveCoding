# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 11:55:01 2021

@author: harshvardhan
"""


def union():
    pass
    
    
def find():
    pass


class Node:
    def __init__(self,parent,rank):
        self.parent = parent 
        self.rank = rank 
        
v,e = map(int,input().split())
edge_list  = [] 
graph = []

for i in range(v):
    temp = Node(i,0)
    graph.append(temp)
for i in range(e):
    e1,e2 = map(int,input().split())
    edge_list.append([e1,e2])



    
    


