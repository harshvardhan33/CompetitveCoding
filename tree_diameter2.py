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

def height_D(root):
    if root is None:
        return 0 
    global res
    lh = height_D(root.left)
    rh = height_D(root.left)
    res = max(res,1+lh+rh)
    return 1+max(lh,rh)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right =Node(5)



res =0
print(height_D(root))