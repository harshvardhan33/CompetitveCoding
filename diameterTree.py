# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 20:27:30 2020

@author: harshvardhan
"""
def height(root):
    if root is None:
        return 0 
    else:
        return 1+max(height(root.left),height(root.right))
def diameter(root):
    if root is None:
        return 0
    d1 = 1 + height(root.left) + height(root.right)
    d2 = diameter(root.left)
    d3 = diameter(root.right)
    return max(d1,max(d2,d3))
    


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
root.left.left.left = Node(8)
root.left.left.left.left = Node(9)
root.left.left.left.left.left = Node(10)
root.left.right.right = Node(8)
root.left.right.right.right =Node(9)

print(diameter(root))