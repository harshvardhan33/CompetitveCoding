# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 23:41:09 2020

@author: harshvardhan
"""

def bfsLine(root):
    if root is None:
        return 
    
    q = []
    q.append(root)
    q.append(None)
    while len(q)>0:
        temp = q[0]
        if temp:
            print(temp.val, end=" ")
            while (q[0]!=None):
                temp = q[0]
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
                
                q.pop(0)
            q.append(None)
        q.pop(0)
                    

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

bfsLine(root)
