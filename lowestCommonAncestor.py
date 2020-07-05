# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 22:27:57 2020

@author: harshvardhan
"""

def lowestAncestor(root,n1,n2):
    if root is None:
        return None 
    if root.val==n1 or root.val==n2:
        return root 
    
    x = lowestAncestor(root.left, n1, n2)
    y = lowestAncestor(root.right, n1, n2)    
    if ((x is not None) and (y is not None)):
        return root 
    if x is not None:
        return x
    else:
        return y 
    
    
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
n1 = 3
n2 = 5
print(lowestAncestor(root, n1, n2).val)