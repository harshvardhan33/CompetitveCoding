# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 00:02:51 2020

@author: harshvardhan
"""


class Node:
    def __init__(self,val):
        self.left = None 
        self.right = None 
        self.val = val
    



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)