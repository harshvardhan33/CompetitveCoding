# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 12:57:40 2020

@author: harshvardhan
"""

def BalancedBT(root):
    if root is None:
        return 0 
    lh = BalancedBT(root.left)
    if lh==-1:
        return -1 
    rh = BalancedBT(root.right)
    if rh==-1:
        return -1
    if abs(lh-rh)>1:
        return -1
    else:
        return 1+max(lh,rh)

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
root.right.right.right =Node(8)

print(BalancedBT(root))

