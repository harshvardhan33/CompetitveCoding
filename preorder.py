# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 14:17:18 2020

@author: harshvardhan
"""

def preorder(root):
    if root is  None:      
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)
    
    
class Node:
    def __init__(self,val):
        self.val =val 
        self.left = None
        self.right =None
    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left= Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)

preorder(root)