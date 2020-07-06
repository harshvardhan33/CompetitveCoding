# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 12:14:36 2020

@author: harshvardhan
"""
def height(root):
    if root is None:
        return 0 
    return 1 + max(height(root.left),height(root.right))


def serialize(root,treeArr,idx):
    if root is None:
        return 
    treeArr[idx-1] = root.val
    serialize(root.left, treeArr, 2*idx)
    serialize(root.right, treeArr,2*idx+1)    
    return
    
def deserialize(root,treeArr,idx,n):
    if idx<=n:
        temp = Node(treeArr[idx-1])
        root = temp 
        root.left = deserialize(root.left, treeArr, idx*2, n)
        root.right = deserialize(root.right, treeArr, idx*2+1, n)
    return root 

 
class Node:
    def __init__(self,val):
        self.val = val 
        self.left = None
        self.right = None
    
    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
n = (2**height(root))-1

treeArr = [None for i in range(n)]
serialize(root, treeArr,1)
x = deserialize(None, treeArr, 1, n)

print("After Deserialize")
print(x.val) 
print(x.left.val) 
print(x.right.val)
print(x.left.left.val) 
print(x.left.right.val)
print(x.right.left.val)
print(x.right.right.val)