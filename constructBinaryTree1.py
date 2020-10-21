# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 22:37:56 2020

@author: harshvardhan
"""

class Node:
    def __init__(self,value):
        self.left =None
        self.right = None
        self.value = value
        
        
        
root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left =Node("F")
root.right.right = Node("G")