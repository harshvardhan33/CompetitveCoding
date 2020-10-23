# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 14:20:34 2020

@author: harshvardhan
"""

class Node:
    def __init__(self,val):
        self.val = val 
        self.left = None
        self.right = None


def searchPath(root,val,path):
    if root is None:
        return False
    if val==root.val:
        path.append(root.val)
        return True
    if val<root.val:
        left = searchPath(root.left,val,path)
        if left==False:
            path.pop()
        else:
            path.append(root.val)
            return True
    if val>root.val:
        right = searchPath(root.right,val,path)
        if right:
            path.append(root.val)
            return True
        else:
            path.pop()
    
    


root = Node(7)
root.left = Node(3)
root.right = Node(12)
root.left.left = Node(1)
root.left.right = Node(5)
root.right.left = Node(10)
root.right.right = Node(14)

path1 = []
path2 = []
searchPath(root,14,path1)
searchPath(root,1,path2)
path1= path1[::-1]
path2 = path2[::-1]
res = None
for i,j in zip(path1,path2):
    if i!=j:
        break
    res = i
print(res)

