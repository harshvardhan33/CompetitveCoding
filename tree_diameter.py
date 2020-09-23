# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 14:57:04 2020

@author: harshvardhan
"""




class Node:
    def __init__(self,val):
        self.left = None 
        self.right = None 
        self.val = val


def height(root):
    if root is None:
        return 0 
    return 1+max(height(root.left),height(root.right))

def diameter(root):
    if root is None:
        return 0
    
    lh = height(root.left)
    rh = height(root.right)
    
    ld = diameter(root.left)
    rd = diameter(root.right)
    
    return max(1+lh+rh,ld,rd)
    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right =Node(5)

print(diameter(root))