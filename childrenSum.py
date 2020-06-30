# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 08:27:48 2020

@author: harshvardhan
"""

def childrenSum(root):
    if root is None:
        return True
    if ((root.left is None) and (root.right is None)):
        return True
    sm = 0 
    if root.left:
        sm+=root.left.val
    if root.right:
        sm+=root.right.val
    
    return (sm==root.val and childrenSum(root.left) and childrenSum(root.right))

class Node:
    def __init__(self,val):
        self.val = val 
        self.left =None 
        self.right = None 

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left= Node(1)
root.left.right=Node(1)
root.right.left=Node(1)
root.right.right=Node(2)


print(childrenSum(root))

