# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 13:54:56 2020

@author: harshvardhan
"""

## Using two for loops 


def bfsTree(root):
    q = []
    q.append(root)

    while len(q)>0:
        count = len(q)
        for i in range(count):
            node = q.pop(0)
            print(node.val,end=" ")
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        print("")
        

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
bfsTree(root)

