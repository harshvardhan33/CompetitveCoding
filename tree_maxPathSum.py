# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 11:36:31 2020

@author: harshvardhan
"""


class Node:
    def __init__(self,val):
        self.left = None 
        self.right = None 
        self.val = val


def maxPathSum(root):
    if root is None:
        return 0
    l_sum = maxPathSum(root.left)
    r_sum = maxPathSum(root.right)
    return max(l_sum+root.val,r_sum+root.val)

root = Node(1)
root.left = Node(1)
root.right = Node(9)
root.left.left = Node(1)
root.left.right =Node(1)
root.right.left = Node(1)
root.right.right = Node(11)


print(maxPathSum(root))