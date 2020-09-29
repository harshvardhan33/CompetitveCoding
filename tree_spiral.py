# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 19:38:19 2020

@author: harshvardhan
"""


def levelOrder(root):
    if root is None:
        return 
    q = []
    stack = []
    q.append(root)
    reverse = False
    while len(q):
        count = len(q)
        for i in range(count):
            curr = q.pop(0)
            if reverse:
                stack.append(curr)
            else:
                print(curr.val,end =" ")
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        if reverse:
            while len(stack):
                print(stack.pop().val,end=" ")
        
        reverse = not(reverse)
        print("")
        


class Node:
    def __init__(self,val):
        self.left = None 
        self.right = None 
        self.val = val
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right =Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

levelOrder(root)