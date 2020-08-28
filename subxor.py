# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 11:16:55 2020

@author: harshvardhan
"""

class TrieNode:
    def __init__(self):
        self.left = None 
        self.right = None 
        


def insert(root,pre_xor):
    curr = root
    for i in range(31,-1,-1):
        curr_bit = (pre_xor>>i)&1
        if curr_bit == 0:
            if curr.left is None:
                curr.left = TrieNode()
            curr =curr.left
        else:
            if curr.right is None:
                curr.right = TrieNode()
            curr = curr.right 
        
        
def queryMax(root,pre_xor):
    curr = root
    curr_xor = 0 
    for i in range(31,-1,-1):
        curr_bit = (pre_xor>>i)&1
        if curr_bit==0:
            if curr.right:
                curr_xor+=2**i
                curr = curr.right
            else:
                curr = curr.left
        else:
            if curr.left:
                curr_xor+=2**i
                curr = curr.left
            else:
                curr = curr.right
    
    return curr_xor            

def maxXor_sub(arr):
    pre_xor = 0
    result = float("-inf")
    root = TrieNode()
    for i in range(len(arr)):
        pre_xor^=arr[i]
        insert(root,pre_xor)
        result = max(result,queryMax(root,pre_xor))
    
    return result
arr = [4,1,3,2,7]
print(maxXor_sub(arr))