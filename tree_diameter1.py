

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

def height(root,dc_h):
    if root is None:
        dc_h[root] = 0 
        return 0
    lh = height(root.left,dc_h)
    rh = height(root.right,dc_h)
    dc_h[root]=1+max(lh,rh) 
    return 1+max(lh,rh)

def diameter(root,dc_h):
    if root is None:
        return 0    
    lh = dc_h[root.left]
    rh = dc_h[root.right]    
    ld = diameter(root.left,dc_h)
    rd = diameter(root.right,dc_h)
    return max(1+lh+rh,ld,rd)
    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right =Node(5)

dc_h ={}
height(root,dc_h)
print(diameter(root, dc_h))





