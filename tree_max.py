# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 14:16:28 2020

@author: harshvardhan
"""

class Node:
    def __init__(self,val):
        self.left = None 
        self.right = None 
        self.val = val
        

def maxTree(root):
    if root is None:
        return float("-inf")
    return max(root.val,maxTree(root.left),maxTree(root.right))



root = Node(100)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(14)
root.left.right =Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(maxTree(root))