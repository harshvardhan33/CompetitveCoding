# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 14:02:23 2020

@author: harshvardhan
"""

def sizeTree(root):
    if root is None:
        return 0
    else:
        return 1+sizeTree(root.left)+sizeTree(root.right)


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
print(sizeTree(root))

