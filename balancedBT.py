# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 08:40:39 2020

@author: harshvardhan
"""
def height(root):
    if root is None:
        return 0 
    l = height(root.left)
    r = height(root.right)
    return 1+max(l,r)

def BalancedBT(root):
    if root is None:
        return True
    else:
        l = height(root.left)
        r = height(root.right)
        ans = abs(l-r)
        if ans<=1:
            return True
        else:
            return False

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
root.right.right.right.right =Node(9)
print(BalancedBT(root))

