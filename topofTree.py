# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 09:52:03 2021

@author: harshvardhan
"""


def fillDist(root,dist):
    if root is None:
        return 
    root.dist = dist
    fillDist(root.left, dist-1)
    fillDist(root.right, dist+1)
    
    
class Node:
    def __init__(self,val):
        self.left = None 
        self.right = None 
        self.val = val
        self.dist = 0 


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


fillDist(root,0)
q=[]
q.append(root)
dc={}
while len(q):
    temp = q.pop(0)
    if temp.dist not in dc:
        dc[temp.dist] = temp.val
    if temp.left:
        q.append(temp.left)
    if temp.right:
        q.append(temp.right)
        

for i in sorted(dc.keys()):
    print(i,dc[i])
