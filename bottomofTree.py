# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 09:55:17 2021

@author: harshvardhan
"""

def giveDist(root,key):
    if root is None:
        return 
    root.dist = key
    giveDist(root.left, key-1)
    giveDist(root.right, key+1)
    
    
class Node:
    def __init__(self,val):
        self.left = None 
        self.right = None 
        self.val = val 
        self.dist =None
        
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.right.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(3)
root.left.right.left = Node(10) 
root.left.right.right = Node(14)
root.right.right = Node(25)


giveDist(root,0)

q = []
q.append(root)
dc = {}
while len(q):
    temp = q.pop(0)
    dc[temp.dist]=temp.val
    if temp.left:
        q.append(temp.left)
    if temp.right:
        q.append(temp.right)
        


for i in sorted(dc.keys()):
    print(dc[i])


