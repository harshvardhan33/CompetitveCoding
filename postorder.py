# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 14:16:05 2020

@author: harshvardhan
"""

def postorder(root):
    if root is  None:      
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)
    
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

postorder(root)